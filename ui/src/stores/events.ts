import { defineStore, acceptHMRUpdate } from "pinia";
import { connect, JSONCodec, credsAuthenticator } from "nats.ws";
import type { NatsConnection, Subscription } from "nats.ws";
import { useAccountStore } from "./account";
import type * as api from "printnanny-api-client";

export const useEventStore = defineStore({
  id: "nats",
  state: () => ({
    events: [] as Array<api.PolymorphicPiEvent | api.PolymorphicPiEventRequest>,
    natsClient: undefined as NatsConnection | undefined,
  }),
  actions: {
    async connect(): Promise<NatsConnection | undefined> {
      // create nats connection if not initialized
      if (this.natsClient === undefined) {
        const account = useAccountStore();
        const nkey = await account.fetchUserNkey();
        if (nkey === undefined) {
          console.warn(
            "Failed to fetch nkey credential. Real-time events will be unavailable."
          );
          return;
        }
        const servers = import.meta.env.VITE_PRINTNANNY_NATS_URI;

        const connectOptions = {
          servers,
          authenticator: credsAuthenticator(
            new TextEncoder().encode(nkey.creds)
          ),
          debug: false,
        };

        if (import.meta.env.VITE_PRINTNANNY_DEBUG == true) {
          connectOptions.debug = true;
        }
        const natsClient = await connect(connectOptions);

        console.log(`Initialized NATs connection to ${servers}`);
        this.$patch({ natsClient });
        return natsClient;
      } else {
        return this.natsClient;
      }
    },

    async publish_command(
      req: api.PolymorphicPiCommandRequest
    ) {
      const natsClient = await this.connect();
      const jsonCodec = JSONCodec<api.PolymorphicPiCommandRequest>();
      const subject = req.subject_pattern.replace("{pi_id}", req.pi.toString());
      await natsClient?.publish(subject, jsonCodec.encode(req));
      console.log(`Published to ${subject}`, req);
    },
    async subscribeAllPis() {
      const natsClient = await this.connect();
      if (natsClient == undefined) {
        return;
      }
      // create a JSON codec/decoder
      const jsonCodec = JSONCodec<api.PolymorphicPiEventRequest>();

      // this subscription listens for all Pi events (scoped to NATs account/org)
      const sub = natsClient.subscribe("pi.>");
      (async (sub: Subscription) => {
        console.log(`Subscribed to ${sub.getSubject()} events...`);
        for await (const msg of sub) {
          const event: api.PolymorphicPiEventRequest = jsonCodec.decode(
            msg.data
          );
          this.handle(event);
          console.log("Deserialized event", event);
        }
        console.log(`subscription ${sub.getSubject()} drained.`);
      })(sub);
    },
    handle(event: api.PolymorphicPiEventRequest) {
      this.events.push(event);
    },
    push(event: api.PolymorphicPiEvent) {
      this.events.push(event);
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useEventStore, import.meta.hot));
}

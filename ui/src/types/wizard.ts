import type { FunctionalComponent, HTMLAttributes, VNodeProps } from "vue";
import { shallowRef } from "vue";

import type { RouteLocationRaw } from "vue-router";
import { CheckIcon, MoonIcon } from "@heroicons/vue/outline";
import { ExclamationCircleIcon } from "@heroicons/vue/solid";
import { JSONCodec, ErrorCode as NatsErrorCode } from "nats.ws";
import type { Subscription, NatsConnection } from "nats.ws";
import * as api from "printnanny-api-client";

import CustomSpinner from "@/components/util/CustomSpinner.vue";
import type { UiAlert, AlertAction } from "./alerts";
import { useAlertStore } from "@/stores/alerts";


export type WizardButton = {
  text: string;
  link: () => RouteLocationRaw;
};

export type WizardStep = {
  key: string;
  title: string;
  detail: string;
  progress: string;
  style: string;
  component: any;
  validationSchema: AnyObjectSchema;
  nextButton: WizardButton | undefined;
  prevButton: WizardButton | undefined;
  onSubmit: (formData: any) => void;
};


export type ManualActionButton = {
  bgColor: string;
  bgColorHover: string;
  bgColorFocus: string;
  text: string;
  onClick: (step: ManualTestStep, stepIdx: number) => void;
  href?: string;
  icon?: FunctionalComponent<HTMLAttributes & VNodeProps>;
};


export class ManualTestStep {
  text: string;
  detail: string;
  icon: FunctionalComponent<HTMLAttributes & VNodeProps>;
  active: boolean;
  done: boolean;
  actions: Array<ManualActionButton>;

  constructor(
    text: string,
    detail: string,
    icon: FunctionalComponent<HTMLAttributes & VNodeProps>,
    actions: Array<ManualActionButton>
  ) {
    this.actions = actions;
    this.detail = detail;
    this.text = text;
    this.icon = icon;
    this.done = false;
    this.active = false;
  }

  public iconBackground(): string {
    if (this.done == true) {
      return "bg-emerald-500";
    } else if (this.active == false) {
      return "bg-gray-400";
    } else {
      return "bg-amber-500";
    }
  }

  public start() {
    this.active = true;
  }

  public finish() {
    this.active = false;
    this.done = true;
  }
}


export type ConnectTestStatusItem = {
  icon: any;
  iconBackground: string;
  text: string;
};

export enum ConnectTestStatus {
  NotStarted = "Not Started",
  Pending = "Pending",
  Success = "Success",
  Error = "Error",
}

export class ConnectTestStep {
  title: string;
  description: string;
  piId: number;
  status: ConnectTestStatus;
  command: api.PolymorphicPiCommandRequest;
  events: Array<api.PolymorphicPiEventRequest>;
  natsClient: NatsConnection;

  icons = {
    [ConnectTestStatus.NotStarted]: {
      icon: MoonIcon,
      iconBackground: "bg-gray-400",
      text: ConnectTestStatus.NotStarted.valueOf(),
    } as ConnectTestStatusItem,
    [ConnectTestStatus.Pending]: {
      icon: shallowRef(CustomSpinner),
      iconBackground: "bg-amber-400",
      text: ConnectTestStatus.Pending.valueOf(),
    } as ConnectTestStatusItem,
    [ConnectTestStatus.Success]: {
      icon: CheckIcon,
      iconBackground: "bg-green-500",
      text: ConnectTestStatus.Success.valueOf(),
    } as ConnectTestStatusItem,
    [ConnectTestStatus.Error]: {
      icon: ExclamationCircleIcon,
      iconBackground: "bg-red-500",
      text: ConnectTestStatus.Error.valueOf(),
    } as ConnectTestStatusItem,
  };
  constructor(
    title: string,
    description: string,
    piId: number,
    command: api.PolymorphicPiCommandRequest,
    natsClient: NatsConnection,
  ) {
    this.title = title;
    this.description = description;
    this.piId = piId;

    this.command = command;

    this.events = [];
    this.natsClient = natsClient;
    this.status = ConnectTestStatus.NotStarted;

  }

  public error(description: string): void {
    this.status = ConnectTestStatus.Error;
    this.description = description;
  }

  public pending(description: string): void {
    this.status = ConnectTestStatus.Pending;
    this.description = description;
  }

  public success(): void {
    this.status = ConnectTestStatus.Success;
  }

  public active(): boolean {
    return this.status === ConnectTestStatus.Pending;
  }

  public statusComponent(): ConnectTestStatusItem {
    return this.icons[this.status];
  }

  public handleEvent(event: api.PolymorphicPiEventRequest) {
    console.log("handling event", event)
    this.events.push(event)
    switch (event.event_type) {
      // PiBootStatusType.SystemctlShow:
      case api.PiBootStatusType.SystemctlShow:
        // get SystemState from payload
        const systemState = event.payload?.SystemState || "unknown"
        switch (systemState) {
          case "degraded":
            this.error("Raspberry Pi is running in a degraded state. Some services may not work. Reboot your Raspberry Pi and refresh this page.");
            break;
          case "starting":
            this.pending("Waiting for Raspberry Pi to finish startup");
            break;
          case "running":
            this.success();
            break
          case "unknown":
            this.error("Raspberry Pi is in an unknown state. Some services may not work as expected. Reboot your Raspberry Pi and refresh this page.")
            break;
          default:
        }
        break;
      case api.PiBootStatusType.SyncSettingsStarted:
        this.pending("Synchronizing with PrintNanny Cloud");
        break;
      case api.PiBootStatusType.SyncSettingsSuccess:
        this.success();
        break;
    }
  }

  public async run(): Promise<void> {
    this.status = ConnectTestStatus.Pending;
    const subject = this.command.subject_pattern.replace("{pi_id}", this.piId);
    const jsonCodec = JSONCodec<api.PolymorphicPiCommandRequest>();

    await this.natsClient.request(subject, jsonCodec.encode(this.command), { timeout: 30000, noMux: true })
      .then((msg) => {
        const reply = jsonCodec.decode(msg.data) as api.PolymorphicPiEventRequest;
        this.handleEvent(reply);
      })
      .catch((e) => {
        const alertStore = useAlertStore();
        if (e.name == "NatsError") {
          const message = "No response from Raspberry Pi. Check that Pi is powered on and connected to Wifi."
          const header = `Connection Error (NATS Service ${e.code})`
          const actions = [{
            color: "red", text: "Refresh", onClick: () => {
              window.location.reload()
            }
          }] as Array<AlertAction>;
          const alert = { error: e, header, message, actions } as UiAlert
          alertStore.push(alert)
        }
        this.status = ConnectTestStatus.Error;
        console.error("Error", e)
      });

  }
}

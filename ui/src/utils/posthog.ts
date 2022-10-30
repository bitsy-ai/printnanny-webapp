import type * as api from "printnanny-api-client";
import posthog from "posthog-js";

function posthogIdentify(user: api.User) {
  // initialize posthog in production only
  if (
    !window.location.href.includes("127.0.0.1") &&
    !window.location.href.includes("localhost")
  ) {
    posthog.identify(
      `user:${user.id}`,
      { email: user.email },
    );
    posthog.alias(
      `user:${user.id}`,
      user.email
    );
    posthog.people.set({ email: user.email })
  }
}

export { posthogIdentify }
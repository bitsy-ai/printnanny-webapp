import type * as api from "printnanny-api-client";
import posthog from "posthog-js";

function posthogIdentify(user: api.User) {
  // initialize posthog in production only
  try {
    if (
      !window.location.href.includes("127.0.0.1") &&
      !window.location.href.includes("localhost")
    ) {
      posthog.identify(`user:${user.id}`, { email: user.email });
      posthog.alias(`user:${user.id}`, user.email);
      posthog.people.set({ email: user.email });
    }
  } catch (error) {
    console.error("posthogIdentify error:", error);
  }
}

function posthogReset() {
  try {
    if (
      !window.location.href.includes("127.0.0.1") &&
      !window.location.href.includes("localhost")
    ) {
      posthog.reset();
    }
  } catch (error) {
    console.error("posthogReset error:", error);
  }
}

export { posthogIdentify, posthogReset };

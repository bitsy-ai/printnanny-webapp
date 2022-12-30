import type * as api from "printnanny-api-client";
import posthog from "posthog-js";
import { useAccountStore } from "@/stores/account";

interface posthogProperties {
  email?: string;
  user_id?: number;
}

function posthogPageview() {
  const queryString = window.location.search;
  const params = new URLSearchParams(queryString);
  const email = params.get("email");
  const userId = params.get("user_id");
  const set: posthogProperties = {};
  if (email) {
    const account = useAccountStore();
    account.$patch({ email: email });
    set["email"] = email;
  }
  if (userId) {
    const account = useAccountStore();
    const userIdInt = parseInt(userId);
    if (userIdInt) {
      account.$patch({ userId: userIdInt });
      set["user_id"] = userIdInt;
    }
  }
  posthog.capture("$pageview", {
    $current_url: window.location.href,
    $set: set,
  });
}

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

export { posthogIdentify, posthogReset, posthogPageview };

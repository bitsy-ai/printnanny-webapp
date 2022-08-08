/**
 * Alert or error message produced by front-end ui code
 */
// import type * as apiTypes from "printnanny-api-client";
import type { FunctionalComponent, HTMLAttributes, VNodeProps } from "vue";
import type { AnyObjectSchema } from "yup";
import type { RouteLocationRaw } from "vue-router";
import type { Moment } from "moment";
import { CheckIcon, MoonIcon } from "@heroicons/vue/outline";
import { ExclamationCircleIcon } from "@heroicons/vue/solid";
import CustomSpinner from "@/components/util/CustomSpinner.vue";
import type * as api from "printnanny-api-client";
import moment from "moment";

export interface AlertAction {
  color: string;
  text: string;
}

export interface UiAlert {
  message: string;
  header: string;
  icon?: FunctionalComponent<HTMLAttributes & VNodeProps>;
  actions: Array<AlertAction>;
  error: Error | undefined;
}

// TODO union of | apiTypes.Alert
// export type Alert = UiAlert | UiAlert;

export type WizardButton = {
  text: string;
  link: () => RouteLocationRaw;
};

export type WizardStep = {
  key: string;
  title: string;
  progress: string;
  style: string;
  component: any;
  validationSchema: AnyObjectSchema;
  nextButton: WizardButton | undefined;
  prevButton: WizardButton | undefined;
  onSubmit: (formData: any) => void;
};

export type ConnectTestStatusItem = {
  icon: any;
  iconBackground: String;
  text: String;
};

export enum ConnectTestStatus {
  NotStarted = "Not Started",
  Pending = "Pending",
  Success = "Success",
  Error = "Error"
};

export class ConnectTestStep {
  content: String;
  status: ConnectTestStatus;
  start_dt?: undefined | Moment;
  end_dt?: undefined | Moment;
  command_event?: undefined | api.PolymorphicPiEventRequest
  status_event?: undefined | api.PolymorphicPiEventRequest
  onPiEvent?: (undefined | ((event: api.PolymorphicPiEventRequest) => void));

  icons = {
    [ConnectTestStatus.NotStarted]: { icon: MoonIcon, iconBackground: "bg-gray-400", text: ConnectTestStatus.NotStarted.valueOf() } as ConnectTestStatusItem,
    [ConnectTestStatus.Pending]: { icon: CustomSpinner, iconBackground: "bg-amber-400", text: ConnectTestStatus.Pending.valueOf() } as ConnectTestStatusItem,
    [ConnectTestStatus.Success]: { icon: CheckIcon, iconBackground: "bg-green-500", text: ConnectTestStatus.Success.valueOf() } as ConnectTestStatusItem,
    [ConnectTestStatus.Error]: { icon: ExclamationCircleIcon, iconBackground: "bg-red-500", text: ConnectTestStatus.Error.valueOf() } as ConnectTestStatusItem
  }
  constructor(content: String, onPiEvent: (undefined | ((event: api.PolymorphicPiEventRequest) => void))) {
    this.content = content;
    this.status = ConnectTestStatus.NotStarted;
    this.command_event = undefined;
    this.status_event = undefined;
    this.start_dt = undefined;
    this.end_dt = undefined;
    this.onPiEvent = onPiEvent;
  }

  public statusText(): string {
    switch (this.status) {
      case ConnectTestStatus.Pending:
        return 'Waiting for Raspberry Pi'
      case ConnectTestStatus.Success:
        return 'Success'
      case ConnectTestStatus.Error:
        return 'Error'
      case ConnectTestStatus.NotStarted:
        return 'Waiting to begin test'
    }
  }

  public active(): boolean {
    return this.status === ConnectTestStatus.Pending
  }


  public statusComponent(): ConnectTestStatusItem {
    return this.icons[this.status]
  }

  public start(event: api.PolymorphicPiEvent): void {
    this.start_dt = moment();
    this.command_event = event;
    this.status = ConnectTestStatus.Pending;

  }

  public handlePiEvent(event: api.PolymorphicPiEventRequest): void {
    if (this.onPiEvent !== undefined) {
      return this.onPiEvent(event)
    }
  }
}


/**
 * Alert or error message produced by front-end ui code
 */
import type * as apiTypes from "printnanny-api-client";
import type { FunctionalComponent, HTMLAttributes, VNodeProps } from "vue";

export interface UiAlert {
    message: string,
    header: String,
    icon?: FunctionalComponent<HTMLAttributes & VNodeProps>
}

export interface UiError extends UiAlert {
    error: Error
}

export type Alert = UiError | UiAlert | apiTypes.Alert

export interface AlertAction {
    color: String,
    text: String,
    onClick: Function
}
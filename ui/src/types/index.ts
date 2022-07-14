
/**
 * Alert or error message produced by front-end ui code
 */
import type * as apiTypes from "printnanny-api-client";

export interface UiAlert {
    message: string,
    header: String
}

export interface UiError extends UiAlert {
    error: Error
}

export type Alert = UiError | UiAlert | apiTypes.Alert
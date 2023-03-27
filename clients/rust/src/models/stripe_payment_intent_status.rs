/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.131.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// StripePaymentIntentStatus : * `canceled` - Cancellation invalidates the intent for future confirmation and cannot be undone. * `processing` - Required actions have been handled. * `requires_action` - Payment Method require additional action, such as 3D secure. * `requires_capture` - Capture the funds on the cards which have been put on holds. * `requires_confirmation` - Intent is ready to be confirmed. * `requires_payment_method` - Intent created and requires a Payment Method to be attached. * `succeeded` - The funds are in your account.

/// * `canceled` - Cancellation invalidates the intent for future confirmation and cannot be undone. * `processing` - Required actions have been handled. * `requires_action` - Payment Method require additional action, such as 3D secure. * `requires_capture` - Capture the funds on the cards which have been put on holds. * `requires_confirmation` - Intent is ready to be confirmed. * `requires_payment_method` - Intent created and requires a Payment Method to be attached. * `succeeded` - The funds are in your account.
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum StripePaymentIntentStatus {
    #[serde(rename = "canceled")]
    Canceled,
    #[serde(rename = "processing")]
    Processing,
    #[serde(rename = "requires_action")]
    RequiresAction,
    #[serde(rename = "requires_capture")]
    RequiresCapture,
    #[serde(rename = "requires_confirmation")]
    RequiresConfirmation,
    #[serde(rename = "requires_payment_method")]
    RequiresPaymentMethod,
    #[serde(rename = "succeeded")]
    Succeeded,

}

impl ToString for StripePaymentIntentStatus {
    fn to_string(&self) -> String {
        match self {
            Self::Canceled => String::from("canceled"),
            Self::Processing => String::from("processing"),
            Self::RequiresAction => String::from("requires_action"),
            Self::RequiresCapture => String::from("requires_capture"),
            Self::RequiresConfirmation => String::from("requires_confirmation"),
            Self::RequiresPaymentMethod => String::from("requires_payment_method"),
            Self::Succeeded => String::from("succeeded"),
        }
    }
}

impl Default for StripePaymentIntentStatus {
    fn default() -> StripePaymentIntentStatus {
        Self::Canceled
    }
}





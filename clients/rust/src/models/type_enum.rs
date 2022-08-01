/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum TypeEnum {
    #[serde(rename = "acss_debit")]
    AcssDebit,
    #[serde(rename = "afterpay_clearpay")]
    AfterpayClearpay,
    #[serde(rename = "alipay")]
    Alipay,
    #[serde(rename = "au_becs_debit")]
    AuBecsDebit,
    #[serde(rename = "bacs_debit")]
    BacsDebit,
    #[serde(rename = "bancontact")]
    Bancontact,
    #[serde(rename = "boleto")]
    Boleto,
    #[serde(rename = "card")]
    Card,
    #[serde(rename = "card_present")]
    CardPresent,
    #[serde(rename = "eps")]
    Eps,
    #[serde(rename = "fpx")]
    Fpx,
    #[serde(rename = "giropay")]
    Giropay,
    #[serde(rename = "grabpay")]
    Grabpay,
    #[serde(rename = "ideal")]
    Ideal,
    #[serde(rename = "interac_present")]
    InteracPresent,
    #[serde(rename = "klarna")]
    Klarna,
    #[serde(rename = "oxxo")]
    Oxxo,
    #[serde(rename = "p24")]
    P24,
    #[serde(rename = "sepa_debit")]
    SepaDebit,
    #[serde(rename = "sofort")]
    Sofort,
    #[serde(rename = "wechat_pay")]
    WechatPay,

}

impl ToString for TypeEnum {
    fn to_string(&self) -> String {
        match self {
            Self::AcssDebit => String::from("acss_debit"),
            Self::AfterpayClearpay => String::from("afterpay_clearpay"),
            Self::Alipay => String::from("alipay"),
            Self::AuBecsDebit => String::from("au_becs_debit"),
            Self::BacsDebit => String::from("bacs_debit"),
            Self::Bancontact => String::from("bancontact"),
            Self::Boleto => String::from("boleto"),
            Self::Card => String::from("card"),
            Self::CardPresent => String::from("card_present"),
            Self::Eps => String::from("eps"),
            Self::Fpx => String::from("fpx"),
            Self::Giropay => String::from("giropay"),
            Self::Grabpay => String::from("grabpay"),
            Self::Ideal => String::from("ideal"),
            Self::InteracPresent => String::from("interac_present"),
            Self::Klarna => String::from("klarna"),
            Self::Oxxo => String::from("oxxo"),
            Self::P24 => String::from("p24"),
            Self::SepaDebit => String::from("sepa_debit"),
            Self::Sofort => String::from("sofort"),
            Self::WechatPay => String::from("wechat_pay"),
        }
    }
}

impl Default for TypeEnum {
    fn default() -> TypeEnum {
        Self::AcssDebit
    }
}





/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.119.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct Product {
    #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
    #[serde(rename = "djstripe_product")]
    pub djstripe_product: Box<crate::models::DjStripeProduct>,
    #[serde(rename = "prices")]
    pub prices: Vec<crate::models::DjStripePrice>,
    #[serde(rename = "deleted")]
    pub deleted: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "sku")]
    pub sku: String,
    #[serde(rename = "slug")]
    pub slug: String,
    #[serde(rename = "unit_label")]
    pub unit_label: String,
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "description")]
    pub description: String,
    #[serde(rename = "statement_descriptor")]
    pub statement_descriptor: String,
    #[serde(rename = "images", skip_serializing_if = "Option::is_none")]
    pub images: Option<Vec<String>>,
    #[serde(rename = "is_active", skip_serializing_if = "Option::is_none")]
    pub is_active: Option<bool>,
    #[serde(rename = "is_shippable")]
    pub is_shippable: bool,
    #[serde(rename = "is_preorder")]
    pub is_preorder: bool,
    #[serde(rename = "is_subscription")]
    pub is_subscription: bool,
    #[serde(rename = "stripe_price_lookup_key", skip_serializing_if = "Option::is_none")]
    pub stripe_price_lookup_key: Option<String>,
    #[serde(rename = "stripe_product_id", skip_serializing_if = "Option::is_none")]
    pub stripe_product_id: Option<String>,
}

impl Product {
    pub fn new(djstripe_product: crate::models::DjStripeProduct, prices: Vec<crate::models::DjStripePrice>, deleted: String, created_dt: String, updated_dt: String, sku: String, slug: String, unit_label: String, name: String, description: String, statement_descriptor: String, is_shippable: bool, is_preorder: bool, is_subscription: bool) -> Product {
        Product {
            id: None,
            djstripe_product: Box::new(djstripe_product),
            prices,
            deleted,
            created_dt,
            updated_dt,
            sku,
            slug,
            unit_label,
            name,
            description,
            statement_descriptor,
            images: None,
            is_active: None,
            is_shippable,
            is_preorder,
            is_subscription,
            stripe_price_lookup_key: None,
            stripe_product_id: None,
        }
    }
}



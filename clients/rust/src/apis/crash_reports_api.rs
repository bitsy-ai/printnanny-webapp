/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.129.7
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


use reqwest;

use bytes::Bytes;
use crate::apis::ResponseContent;
use super::{Error, configuration};


/// struct for typed errors of method [`crash_reports_create`]
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(untagged)]
pub enum CrashReportsCreateError {
    Status409(crate::models::ErrorDetail),
    Status400(crate::models::ErrorDetail),
    Status401(crate::models::ErrorDetail),
    Status403(crate::models::ErrorDetail),
    Status500(crate::models::ErrorDetail),
    UnknownValue(serde_json::Value),
}

/// struct for typed errors of method [`crash_reports_list`]
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(untagged)]
pub enum CrashReportsListError {
    Status400(crate::models::ErrorDetail),
    Status401(crate::models::ErrorDetail),
    Status403(crate::models::ErrorDetail),
    Status500(crate::models::ErrorDetail),
    UnknownValue(serde_json::Value),
}

/// struct for typed errors of method [`crash_reports_partial_update`]
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(untagged)]
pub enum CrashReportsPartialUpdateError {
    Status409(crate::models::ErrorDetail),
    Status400(crate::models::ErrorDetail),
    Status401(crate::models::ErrorDetail),
    Status403(crate::models::ErrorDetail),
    Status500(crate::models::ErrorDetail),
    UnknownValue(serde_json::Value),
}

/// struct for typed errors of method [`crash_reports_retrieve`]
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(untagged)]
pub enum CrashReportsRetrieveError {
    UnknownValue(serde_json::Value),
}

/// struct for typed errors of method [`crash_reports_update`]
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(untagged)]
pub enum CrashReportsUpdateError {
    Status409(crate::models::ErrorDetail),
    Status400(crate::models::ErrorDetail),
    Status401(crate::models::ErrorDetail),
    Status403(crate::models::ErrorDetail),
    Status500(crate::models::ErrorDetail),
    UnknownValue(serde_json::Value),
}


pub async fn crash_reports_create(configuration: &configuration::Configuration, description: Option<&str>, email: Option<&str>, os_version: Option<&str>, os_logs: Option<std::path::PathBuf>, browser_version: Option<&str>, browser_logs: Option<std::path::PathBuf>, serial: Option<&str>, posthog_session: Option<&str>, status: Option<crate::models::CrashReportStatusEnum>, support_comment: Option<&str>, pi: Option<i32>) -> Result<crate::models::CrashReport, Error<CrashReportsCreateError>> {
    let local_var_configuration = configuration;

    let local_var_client = &local_var_configuration.client;

    let local_var_uri_str = format!("{}/api/crash-reports/", local_var_configuration.base_path);
    let mut local_var_req_builder = local_var_client.request(reqwest::Method::POST, local_var_uri_str.as_str());

    if let Some(ref local_var_user_agent) = local_var_configuration.user_agent {
        local_var_req_builder = local_var_req_builder.header(reqwest::header::USER_AGENT, local_var_user_agent.clone());
    }
    if let Some(ref local_var_token) = local_var_configuration.bearer_access_token {
        local_var_req_builder = local_var_req_builder.bearer_auth(local_var_token.to_owned());
    };
    let mut local_var_form = reqwest::multipart::Form::new();
    if let Some(local_var_param_value) = description {
        local_var_form = local_var_form.text("description", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = email {
        local_var_form = local_var_form.text("email", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = os_version {
        local_var_form = local_var_form.text("os_version", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = os_logs {
        let kind = infer::get_from_path(&local_var_param_value)?.unwrap();
        let filebytes = tokio::fs::read(&local_var_param_value).await?;
        let file_part = reqwest::multipart::Part::bytes(filebytes)
            .file_name(local_var_param_value.display().to_string())
            .mime_str(kind.mime_type())?;
        local_var_form = local_var_form.part("os_logs", file_part);
    }
    if let Some(local_var_param_value) = browser_version {
        local_var_form = local_var_form.text("browser_version", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = browser_logs {
        let kind = infer::get_from_path(&local_var_param_value)?.unwrap();
        let filebytes = tokio::fs::read(&local_var_param_value).await?;
        let file_part = reqwest::multipart::Part::bytes(filebytes)
            .file_name(local_var_param_value.display().to_string())
            .mime_str(kind.mime_type())?;
        local_var_form = local_var_form.part("browser_logs", file_part);
    }
    if let Some(local_var_param_value) = serial {
        local_var_form = local_var_form.text("serial", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = posthog_session {
        local_var_form = local_var_form.text("posthog_session", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = status {
        local_var_form = local_var_form.text("status", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = support_comment {
        local_var_form = local_var_form.text("support_comment", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = pi {
        local_var_form = local_var_form.text("pi", local_var_param_value.to_string());
    }
    local_var_req_builder = local_var_req_builder.multipart(local_var_form);

    let local_var_req = local_var_req_builder.build()?;
    let local_var_resp = local_var_client.execute(local_var_req).await?;

    let local_var_status = local_var_resp.status();
    let local_var_content = local_var_resp.text().await?;

    if !local_var_status.is_client_error() && !local_var_status.is_server_error() {
        serde_json::from_str(&local_var_content).map_err(Error::from)
    } else {
        let local_var_entity: Option<CrashReportsCreateError> = serde_json::from_str(&local_var_content).ok();
        let local_var_error = ResponseContent { status: local_var_status, content: local_var_content, entity: local_var_entity };
        Err(Error::ResponseError(local_var_error))
    }
}

pub async fn crash_reports_list(configuration: &configuration::Configuration, page: Option<i32>) -> Result<crate::models::PaginatedCrashReportList, Error<CrashReportsListError>> {
    let local_var_configuration = configuration;

    let local_var_client = &local_var_configuration.client;

    let local_var_uri_str = format!("{}/api/crash-reports/", local_var_configuration.base_path);
    let mut local_var_req_builder = local_var_client.request(reqwest::Method::GET, local_var_uri_str.as_str());

    if let Some(ref local_var_str) = page {
        local_var_req_builder = local_var_req_builder.query(&[("page", &local_var_str.to_string())]);
    }
    if let Some(ref local_var_user_agent) = local_var_configuration.user_agent {
        local_var_req_builder = local_var_req_builder.header(reqwest::header::USER_AGENT, local_var_user_agent.clone());
    }
    if let Some(ref local_var_token) = local_var_configuration.bearer_access_token {
        local_var_req_builder = local_var_req_builder.bearer_auth(local_var_token.to_owned());
    };

    let local_var_req = local_var_req_builder.build()?;
    let local_var_resp = local_var_client.execute(local_var_req).await?;

    let local_var_status = local_var_resp.status();
    let local_var_content = local_var_resp.text().await?;

    if !local_var_status.is_client_error() && !local_var_status.is_server_error() {
        serde_json::from_str(&local_var_content).map_err(Error::from)
    } else {
        let local_var_entity: Option<CrashReportsListError> = serde_json::from_str(&local_var_content).ok();
        let local_var_error = ResponseContent { status: local_var_status, content: local_var_content, entity: local_var_entity };
        Err(Error::ResponseError(local_var_error))
    }
}

pub async fn crash_reports_partial_update(configuration: &configuration::Configuration, id: &str, description: Option<&str>, email: Option<&str>, os_version: Option<&str>, os_logs: Option<std::path::PathBuf>, browser_version: Option<&str>, browser_logs: Option<std::path::PathBuf>, serial: Option<&str>, posthog_session: Option<&str>, status: Option<crate::models::CrashReportStatusEnum>, support_comment: Option<&str>, pi: Option<i32>) -> Result<crate::models::CrashReport, Error<CrashReportsPartialUpdateError>> {
    let local_var_configuration = configuration;

    let local_var_client = &local_var_configuration.client;

    let local_var_uri_str = format!("{}/api/crash-reports/{id}/", local_var_configuration.base_path, id=crate::apis::urlencode(id));
    let mut local_var_req_builder = local_var_client.request(reqwest::Method::PATCH, local_var_uri_str.as_str());

    if let Some(ref local_var_user_agent) = local_var_configuration.user_agent {
        local_var_req_builder = local_var_req_builder.header(reqwest::header::USER_AGENT, local_var_user_agent.clone());
    }
    if let Some(ref local_var_token) = local_var_configuration.bearer_access_token {
        local_var_req_builder = local_var_req_builder.bearer_auth(local_var_token.to_owned());
    };
    let mut local_var_form = reqwest::multipart::Form::new();
    if let Some(local_var_param_value) = description {
        local_var_form = local_var_form.text("description", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = email {
        local_var_form = local_var_form.text("email", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = os_version {
        local_var_form = local_var_form.text("os_version", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = os_logs {
        let kind = infer::get_from_path(&local_var_param_value)?.unwrap();
        let filebytes = tokio::fs::read(&local_var_param_value).await?;
        let file_part = reqwest::multipart::Part::bytes(filebytes)
            .file_name(local_var_param_value.display().to_string())
            .mime_str(kind.mime_type())?;
        local_var_form = local_var_form.part("os_logs", file_part);
    }
    if let Some(local_var_param_value) = browser_version {
        local_var_form = local_var_form.text("browser_version", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = browser_logs {
        let kind = infer::get_from_path(&local_var_param_value)?.unwrap();
        let filebytes = tokio::fs::read(&local_var_param_value).await?;
        let file_part = reqwest::multipart::Part::bytes(filebytes)
            .file_name(local_var_param_value.display().to_string())
            .mime_str(kind.mime_type())?;
        local_var_form = local_var_form.part("browser_logs", file_part);
    }
    if let Some(local_var_param_value) = serial {
        local_var_form = local_var_form.text("serial", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = posthog_session {
        local_var_form = local_var_form.text("posthog_session", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = status {
        local_var_form = local_var_form.text("status", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = support_comment {
        local_var_form = local_var_form.text("support_comment", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = pi {
        local_var_form = local_var_form.text("pi", local_var_param_value.to_string());
    }
    local_var_req_builder = local_var_req_builder.multipart(local_var_form);

    let local_var_req = local_var_req_builder.build()?;
    let local_var_resp = local_var_client.execute(local_var_req).await?;

    let local_var_status = local_var_resp.status();
    let local_var_content = local_var_resp.text().await?;

    if !local_var_status.is_client_error() && !local_var_status.is_server_error() {
        serde_json::from_str(&local_var_content).map_err(Error::from)
    } else {
        let local_var_entity: Option<CrashReportsPartialUpdateError> = serde_json::from_str(&local_var_content).ok();
        let local_var_error = ResponseContent { status: local_var_status, content: local_var_content, entity: local_var_entity };
        Err(Error::ResponseError(local_var_error))
    }
}

pub async fn crash_reports_retrieve(configuration: &configuration::Configuration, id: &str) -> Result<crate::models::CrashReport, Error<CrashReportsRetrieveError>> {
    let local_var_configuration = configuration;

    let local_var_client = &local_var_configuration.client;

    let local_var_uri_str = format!("{}/api/crash-reports/{id}/", local_var_configuration.base_path, id=crate::apis::urlencode(id));
    let mut local_var_req_builder = local_var_client.request(reqwest::Method::GET, local_var_uri_str.as_str());

    if let Some(ref local_var_user_agent) = local_var_configuration.user_agent {
        local_var_req_builder = local_var_req_builder.header(reqwest::header::USER_AGENT, local_var_user_agent.clone());
    }
    if let Some(ref local_var_token) = local_var_configuration.bearer_access_token {
        local_var_req_builder = local_var_req_builder.bearer_auth(local_var_token.to_owned());
    };

    let local_var_req = local_var_req_builder.build()?;
    let local_var_resp = local_var_client.execute(local_var_req).await?;

    let local_var_status = local_var_resp.status();
    let local_var_content = local_var_resp.text().await?;

    if !local_var_status.is_client_error() && !local_var_status.is_server_error() {
        serde_json::from_str(&local_var_content).map_err(Error::from)
    } else {
        let local_var_entity: Option<CrashReportsRetrieveError> = serde_json::from_str(&local_var_content).ok();
        let local_var_error = ResponseContent { status: local_var_status, content: local_var_content, entity: local_var_entity };
        Err(Error::ResponseError(local_var_error))
    }
}

pub async fn crash_reports_update(configuration: &configuration::Configuration, id: &str, description: Option<&str>, email: Option<&str>, os_version: Option<&str>, os_logs: Option<std::path::PathBuf>, browser_version: Option<&str>, browser_logs: Option<std::path::PathBuf>, serial: Option<&str>, posthog_session: Option<&str>, status: Option<crate::models::CrashReportStatusEnum>, support_comment: Option<&str>, pi: Option<i32>) -> Result<crate::models::CrashReport, Error<CrashReportsUpdateError>> {
    let local_var_configuration = configuration;

    let local_var_client = &local_var_configuration.client;

    let local_var_uri_str = format!("{}/api/crash-reports/{id}/", local_var_configuration.base_path, id=crate::apis::urlencode(id));
    let mut local_var_req_builder = local_var_client.request(reqwest::Method::PUT, local_var_uri_str.as_str());

    if let Some(ref local_var_user_agent) = local_var_configuration.user_agent {
        local_var_req_builder = local_var_req_builder.header(reqwest::header::USER_AGENT, local_var_user_agent.clone());
    }
    if let Some(ref local_var_token) = local_var_configuration.bearer_access_token {
        local_var_req_builder = local_var_req_builder.bearer_auth(local_var_token.to_owned());
    };
    let mut local_var_form = reqwest::multipart::Form::new();
    if let Some(local_var_param_value) = description {
        local_var_form = local_var_form.text("description", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = email {
        local_var_form = local_var_form.text("email", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = os_version {
        local_var_form = local_var_form.text("os_version", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = os_logs {
        let kind = infer::get_from_path(&local_var_param_value)?.unwrap();
        let filebytes = tokio::fs::read(&local_var_param_value).await?;
        let file_part = reqwest::multipart::Part::bytes(filebytes)
            .file_name(local_var_param_value.display().to_string())
            .mime_str(kind.mime_type())?;
        local_var_form = local_var_form.part("os_logs", file_part);
    }
    if let Some(local_var_param_value) = browser_version {
        local_var_form = local_var_form.text("browser_version", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = browser_logs {
        let kind = infer::get_from_path(&local_var_param_value)?.unwrap();
        let filebytes = tokio::fs::read(&local_var_param_value).await?;
        let file_part = reqwest::multipart::Part::bytes(filebytes)
            .file_name(local_var_param_value.display().to_string())
            .mime_str(kind.mime_type())?;
        local_var_form = local_var_form.part("browser_logs", file_part);
    }
    if let Some(local_var_param_value) = serial {
        local_var_form = local_var_form.text("serial", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = posthog_session {
        local_var_form = local_var_form.text("posthog_session", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = status {
        local_var_form = local_var_form.text("status", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = support_comment {
        local_var_form = local_var_form.text("support_comment", local_var_param_value.to_string());
    }
    if let Some(local_var_param_value) = pi {
        local_var_form = local_var_form.text("pi", local_var_param_value.to_string());
    }
    local_var_req_builder = local_var_req_builder.multipart(local_var_form);

    let local_var_req = local_var_req_builder.build()?;
    let local_var_resp = local_var_client.execute(local_var_req).await?;

    let local_var_status = local_var_resp.status();
    let local_var_content = local_var_resp.text().await?;

    if !local_var_status.is_client_error() && !local_var_status.is_server_error() {
        serde_json::from_str(&local_var_content).map_err(Error::from)
    } else {
        let local_var_entity: Option<CrashReportsUpdateError> = serde_json::from_str(&local_var_content).ok();
        let local_var_error = ResponseContent { status: local_var_status, content: local_var_content, entity: local_var_entity };
        Err(Error::ResponseError(local_var_error))
    }
}



# Nested

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **kotlin.Int** |  |  [readonly]
**password** | **kotlin.String** |  | 
**email** | **kotlin.String** |  | 
**isSuperuser** | **kotlin.Boolean** |  |  [optional]
**isStaff** | **kotlin.Boolean** |  |  [optional]
**isActive** | **kotlin.Boolean** |  |  [optional]
**dateJoined** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional]
**lastLogin** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional]
**firstName** | **kotlin.String** |  |  [optional]
**lastName** | **kotlin.String** |  |  [optional]
**groups** | **kotlin.collections.List&lt;kotlin.Int&gt;** | The groups this user belongs to. A user will get all permissions granted to each of their groups. |  [optional]
**userPermissions** | **kotlin.collections.List&lt;kotlin.Int&gt;** | Specific permissions for this user. |  [optional]




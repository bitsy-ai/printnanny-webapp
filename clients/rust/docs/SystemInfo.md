# SystemInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**created_dt** | **String** |  | [readonly]
**updated_dt** | **String** |  | [readonly]
**machine_id** | **String** | Populated from /etc/machine-id | 
**hardware** | **String** | Populated from /proc/cpuinfo HARDWARE | 
**revision** | **String** | Populated from /proc/cpuinfo REVISION | 
**model** | **String** | Populated from /proc/cpuinfo MODEL | 
**serial** | **String** | Populated from /proc/cpuinfo SERIAL | 
**cores** | **i32** |  | 
**ram** | **i64** |  | 
**image_version** | **String** | PrintNanny OS image version string from /boot/image_version.txt | 
**ansible_collection_version** | **String** | PrintNanny OS ansible collection version string. Releaes: https://github.com/bitsy-ai/ansible-collection-printnanny | 
**device** | **i32** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



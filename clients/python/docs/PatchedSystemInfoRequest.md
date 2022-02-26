# PatchedSystemInfoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_id** | **str** | Populated from /etc/machine-id | [optional] 
**hardware** | **str** | Populated from /proc/cpuinfo HARDWARE | [optional] 
**revision** | **str** | Populated from /proc/cpuinfo REVISION | [optional] 
**model** | **str** | Populated from /proc/cpuinfo MODEL | [optional] 
**serial** | **str** | Populated from /proc/cpuinfo SERIAL | [optional] 
**cores** | **int** |  | [optional] 
**ram** | **int** |  | [optional] 
**image_version** | **str** | PrintNanny OS image version string from /boot/image_version.txt | [optional] 
**ansible_collection_version** | **str** | PrintNanny OS ansible collection version string. Releaes: https://github.com/bitsy-ai/ansible-collection-printnanny | [optional] 
**device** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



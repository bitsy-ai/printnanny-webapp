# SystemInfoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_id** | **str** | Populated from /etc/machine-id | 
**hardware** | **str** | Populated from /proc/cpuinfo HARDWARE | 
**revision** | **str** | Populated from /proc/cpuinfo REVISION | 
**model** | **str** | Populated from /proc/cpuinfo MODEL | 
**serial** | **str** | Populated from /proc/cpuinfo SERIAL | 
**cores** | **int** |  | 
**ram** | **int** |  | 
**image_version** | **str** | PrintNanny OS image version string from /boot/image_version.txt | 
**ansible_collection_version** | **str** | PrintNanny OS ansible collection version string. Releaes: https://github.com/bitsy-ai/ansible-collection-printnanny | 
**device** | **int** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



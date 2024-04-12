# ConfigurationDetails200ResponseImages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** |  | [optional] 
**secure_base_url** | **str** |  | [optional] 
**backdrop_sizes** | **List[str]** |  | [optional] 
**logo_sizes** | **List[str]** |  | [optional] 
**poster_sizes** | **List[str]** |  | [optional] 
**profile_sizes** | **List[str]** |  | [optional] 
**still_sizes** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.configuration_details200_response_images import ConfigurationDetails200ResponseImages

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationDetails200ResponseImages from a JSON string
configuration_details200_response_images_instance = ConfigurationDetails200ResponseImages.from_json(json)
# print the JSON string representation of the object
print(ConfigurationDetails200ResponseImages.to_json())

# convert the object into a dict
configuration_details200_response_images_dict = configuration_details200_response_images_instance.to_dict()
# create an instance of ConfigurationDetails200ResponseImages from a dict
configuration_details200_response_images_from_dict = ConfigurationDetails200ResponseImages.from_dict(configuration_details200_response_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



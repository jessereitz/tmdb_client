# ConfigurationDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | [**ConfigurationDetails200ResponseImages**](ConfigurationDetails200ResponseImages.md) |  | [optional] 
**change_keys** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.configuration_details200_response import ConfigurationDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationDetails200Response from a JSON string
configuration_details200_response_instance = ConfigurationDetails200Response.from_json(json)
# print the JSON string representation of the object
print(ConfigurationDetails200Response.to_json())

# convert the object into a dict
configuration_details200_response_dict = configuration_details200_response_instance.to_dict()
# create an instance of ConfigurationDetails200Response from a dict
configuration_details200_response_from_dict = ConfigurationDetails200Response.from_dict(configuration_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ConfigurationLanguages200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_639_1** | **str** |  | [optional] 
**english_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.configuration_languages200_response_inner import ConfigurationLanguages200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationLanguages200ResponseInner from a JSON string
configuration_languages200_response_inner_instance = ConfigurationLanguages200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ConfigurationLanguages200ResponseInner.to_json())

# convert the object into a dict
configuration_languages200_response_inner_dict = configuration_languages200_response_inner_instance.to_dict()
# create an instance of ConfigurationLanguages200ResponseInner from a dict
configuration_languages200_response_inner_from_dict = ConfigurationLanguages200ResponseInner.from_dict(configuration_languages200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



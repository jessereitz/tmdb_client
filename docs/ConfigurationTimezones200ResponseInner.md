# ConfigurationTimezones200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_1** | **str** |  | [optional] 
**zones** | **List[str]** |  | [optional] 

## Example

```python
from tmdb_client.models.configuration_timezones200_response_inner import ConfigurationTimezones200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationTimezones200ResponseInner from a JSON string
configuration_timezones200_response_inner_instance = ConfigurationTimezones200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ConfigurationTimezones200ResponseInner.to_json())

# convert the object into a dict
configuration_timezones200_response_inner_dict = configuration_timezones200_response_inner_instance.to_dict()
# create an instance of ConfigurationTimezones200ResponseInner from a dict
configuration_timezones200_response_inner_from_dict = ConfigurationTimezones200ResponseInner.from_dict(configuration_timezones200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ConfigurationJobs200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**department** | **str** |  | [optional] 
**jobs** | **List[str]** |  | [optional] 

## Example

```python
from tmdb_client.models.configuration_jobs200_response_inner import ConfigurationJobs200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationJobs200ResponseInner from a JSON string
configuration_jobs200_response_inner_instance = ConfigurationJobs200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ConfigurationJobs200ResponseInner.to_json())

# convert the object into a dict
configuration_jobs200_response_inner_dict = configuration_jobs200_response_inner_instance.to_dict()
# create an instance of ConfigurationJobs200ResponseInner from a dict
configuration_jobs200_response_inner_from_dict = ConfigurationJobs200ResponseInner.from_dict(configuration_jobs200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



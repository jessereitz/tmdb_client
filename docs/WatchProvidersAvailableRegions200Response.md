# WatchProvidersAvailableRegions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[WatchProvidersAvailableRegions200ResponseResultsInner]**](WatchProvidersAvailableRegions200ResponseResultsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.watch_providers_available_regions200_response import WatchProvidersAvailableRegions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of WatchProvidersAvailableRegions200Response from a JSON string
watch_providers_available_regions200_response_instance = WatchProvidersAvailableRegions200Response.from_json(json)
# print the JSON string representation of the object
print(WatchProvidersAvailableRegions200Response.to_json())

# convert the object into a dict
watch_providers_available_regions200_response_dict = watch_providers_available_regions200_response_instance.to_dict()
# create an instance of WatchProvidersAvailableRegions200Response from a dict
watch_providers_available_regions200_response_from_dict = WatchProvidersAvailableRegions200Response.from_dict(watch_providers_available_regions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



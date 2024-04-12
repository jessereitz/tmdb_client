# WatchProvidersAvailableRegions200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_1** | **str** |  | [optional] 
**english_name** | **str** |  | [optional] 
**native_name** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.watch_providers_available_regions200_response_results_inner import WatchProvidersAvailableRegions200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WatchProvidersAvailableRegions200ResponseResultsInner from a JSON string
watch_providers_available_regions200_response_results_inner_instance = WatchProvidersAvailableRegions200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(WatchProvidersAvailableRegions200ResponseResultsInner.to_json())

# convert the object into a dict
watch_providers_available_regions200_response_results_inner_dict = watch_providers_available_regions200_response_results_inner_instance.to_dict()
# create an instance of WatchProvidersAvailableRegions200ResponseResultsInner from a dict
watch_providers_available_regions200_response_results_inner_from_dict = WatchProvidersAvailableRegions200ResponseResultsInner.from_dict(watch_providers_available_regions200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



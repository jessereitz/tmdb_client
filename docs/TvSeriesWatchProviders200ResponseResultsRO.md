# TvSeriesWatchProviders200ResponseResultsRO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsROFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsROFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_ro import TvSeriesWatchProviders200ResponseResultsRO

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsRO from a JSON string
tv_series_watch_providers200_response_results_ro_instance = TvSeriesWatchProviders200ResponseResultsRO.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsRO.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_ro_dict = tv_series_watch_providers200_response_results_ro_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsRO from a dict
tv_series_watch_providers200_response_results_ro_from_dict = TvSeriesWatchProviders200ResponseResultsRO.from_dict(tv_series_watch_providers200_response_results_ro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



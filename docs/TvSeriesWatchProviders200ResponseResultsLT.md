# TvSeriesWatchProviders200ResponseResultsLT


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsLTRentInner]**](MovieWatchProviders200ResponseResultsLTRentInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_lt import TvSeriesWatchProviders200ResponseResultsLT

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsLT from a JSON string
tv_series_watch_providers200_response_results_lt_instance = TvSeriesWatchProviders200ResponseResultsLT.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsLT.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_lt_dict = tv_series_watch_providers200_response_results_lt_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsLT from a dict
tv_series_watch_providers200_response_results_lt_from_dict = TvSeriesWatchProviders200ResponseResultsLT.from_dict(tv_series_watch_providers200_response_results_lt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



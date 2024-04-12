# TvSeriesWatchProviders200ResponseResultsRU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsRUFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsRUFlatrateInner.md) |  | [optional] 
**ads** | [**List[TvSeriesWatchProviders200ResponseResultsRUAdsInner]**](TvSeriesWatchProviders200ResponseResultsRUAdsInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_ru import TvSeriesWatchProviders200ResponseResultsRU

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsRU from a JSON string
tv_series_watch_providers200_response_results_ru_instance = TvSeriesWatchProviders200ResponseResultsRU.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsRU.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_ru_dict = tv_series_watch_providers200_response_results_ru_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsRU from a dict
tv_series_watch_providers200_response_results_ru_from_dict = TvSeriesWatchProviders200ResponseResultsRU.from_dict(tv_series_watch_providers200_response_results_ru_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



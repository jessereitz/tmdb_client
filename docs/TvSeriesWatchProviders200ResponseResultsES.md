# TvSeriesWatchProviders200ResponseResultsES


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsESFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsESFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_es import TvSeriesWatchProviders200ResponseResultsES

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsES from a JSON string
tv_series_watch_providers200_response_results_es_instance = TvSeriesWatchProviders200ResponseResultsES.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsES.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_es_dict = tv_series_watch_providers200_response_results_es_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsES from a dict
tv_series_watch_providers200_response_results_es_from_dict = TvSeriesWatchProviders200ResponseResultsES.from_dict(tv_series_watch_providers200_response_results_es_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



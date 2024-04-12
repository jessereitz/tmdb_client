# TvSeriesWatchProviders200ResponseResultsTW


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsHKFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsHKFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_tw import TvSeriesWatchProviders200ResponseResultsTW

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsTW from a JSON string
tv_series_watch_providers200_response_results_tw_instance = TvSeriesWatchProviders200ResponseResultsTW.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsTW.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_tw_dict = tv_series_watch_providers200_response_results_tw_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsTW from a dict
tv_series_watch_providers200_response_results_tw_from_dict = TvSeriesWatchProviders200ResponseResultsTW.from_dict(tv_series_watch_providers200_response_results_tw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



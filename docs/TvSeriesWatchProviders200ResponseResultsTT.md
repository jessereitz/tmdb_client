# TvSeriesWatchProviders200ResponseResultsTT


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsTTFlatrateInner]**](MovieWatchProviders200ResponseResultsTTFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_tt import TvSeriesWatchProviders200ResponseResultsTT

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsTT from a JSON string
tv_series_watch_providers200_response_results_tt_instance = TvSeriesWatchProviders200ResponseResultsTT.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsTT.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_tt_dict = tv_series_watch_providers200_response_results_tt_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsTT from a dict
tv_series_watch_providers200_response_results_tt_from_dict = TvSeriesWatchProviders200ResponseResultsTT.from_dict(tv_series_watch_providers200_response_results_tt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



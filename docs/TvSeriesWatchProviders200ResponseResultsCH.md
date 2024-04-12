# TvSeriesWatchProviders200ResponseResultsCH


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsCHFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsCHFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsPERentInner]**](MovieWatchProviders200ResponseResultsPERentInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_ch import TvSeriesWatchProviders200ResponseResultsCH

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsCH from a JSON string
tv_series_watch_providers200_response_results_ch_instance = TvSeriesWatchProviders200ResponseResultsCH.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsCH.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_ch_dict = tv_series_watch_providers200_response_results_ch_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsCH from a dict
tv_series_watch_providers200_response_results_ch_from_dict = TvSeriesWatchProviders200ResponseResultsCH.from_dict(tv_series_watch_providers200_response_results_ch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



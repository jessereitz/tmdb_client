# TvSeriesWatchProviders200ResponseResultsBG


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsBGFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsBGFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_bg import TvSeriesWatchProviders200ResponseResultsBG

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsBG from a JSON string
tv_series_watch_providers200_response_results_bg_instance = TvSeriesWatchProviders200ResponseResultsBG.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsBG.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_bg_dict = tv_series_watch_providers200_response_results_bg_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsBG from a dict
tv_series_watch_providers200_response_results_bg_from_dict = TvSeriesWatchProviders200ResponseResultsBG.from_dict(tv_series_watch_providers200_response_results_bg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



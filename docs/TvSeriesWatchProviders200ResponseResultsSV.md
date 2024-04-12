# TvSeriesWatchProviders200ResponseResultsSV


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsSVFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsSVFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_sv import TvSeriesWatchProviders200ResponseResultsSV

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsSV from a JSON string
tv_series_watch_providers200_response_results_sv_instance = TvSeriesWatchProviders200ResponseResultsSV.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsSV.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_sv_dict = tv_series_watch_providers200_response_results_sv_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsSV from a dict
tv_series_watch_providers200_response_results_sv_from_dict = TvSeriesWatchProviders200ResponseResultsSV.from_dict(tv_series_watch_providers200_response_results_sv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



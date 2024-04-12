# TvSeriesWatchProviders200ResponseResultsPH


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsPHFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsPHFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_ph import TvSeriesWatchProviders200ResponseResultsPH

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsPH from a JSON string
tv_series_watch_providers200_response_results_ph_instance = TvSeriesWatchProviders200ResponseResultsPH.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsPH.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_ph_dict = tv_series_watch_providers200_response_results_ph_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsPH from a dict
tv_series_watch_providers200_response_results_ph_from_dict = TvSeriesWatchProviders200ResponseResultsPH.from_dict(tv_series_watch_providers200_response_results_ph_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



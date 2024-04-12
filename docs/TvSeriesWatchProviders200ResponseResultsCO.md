# TvSeriesWatchProviders200ResponseResultsCO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsCOFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsCOFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_co import TvSeriesWatchProviders200ResponseResultsCO

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsCO from a JSON string
tv_series_watch_providers200_response_results_co_instance = TvSeriesWatchProviders200ResponseResultsCO.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsCO.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_co_dict = tv_series_watch_providers200_response_results_co_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsCO from a dict
tv_series_watch_providers200_response_results_co_from_dict = TvSeriesWatchProviders200ResponseResultsCO.from_dict(tv_series_watch_providers200_response_results_co_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



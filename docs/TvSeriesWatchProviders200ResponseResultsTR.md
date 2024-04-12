# TvSeriesWatchProviders200ResponseResultsTR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsTRFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsTRFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_tr import TvSeriesWatchProviders200ResponseResultsTR

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsTR from a JSON string
tv_series_watch_providers200_response_results_tr_instance = TvSeriesWatchProviders200ResponseResultsTR.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsTR.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_tr_dict = tv_series_watch_providers200_response_results_tr_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsTR from a dict
tv_series_watch_providers200_response_results_tr_from_dict = TvSeriesWatchProviders200ResponseResultsTR.from_dict(tv_series_watch_providers200_response_results_tr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TvSeriesWatchProviders200ResponseResultsNO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsARFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsARFlatrateInner.md) |  | [optional] 
**buy** | [**List[TvSeriesWatchProviders200ResponseResultsNOBuyInner]**](TvSeriesWatchProviders200ResponseResultsNOBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_no import TvSeriesWatchProviders200ResponseResultsNO

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsNO from a JSON string
tv_series_watch_providers200_response_results_no_instance = TvSeriesWatchProviders200ResponseResultsNO.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsNO.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_no_dict = tv_series_watch_providers200_response_results_no_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsNO from a dict
tv_series_watch_providers200_response_results_no_from_dict = TvSeriesWatchProviders200ResponseResultsNO.from_dict(tv_series_watch_providers200_response_results_no_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



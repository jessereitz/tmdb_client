# TvSeriesWatchProviders200ResponseResultsIT


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[TvSeriesWatchProviders200ResponseResultsITBuyInner]**](TvSeriesWatchProviders200ResponseResultsITBuyInner.md) |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsIEFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsIEFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_it import TvSeriesWatchProviders200ResponseResultsIT

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsIT from a JSON string
tv_series_watch_providers200_response_results_it_instance = TvSeriesWatchProviders200ResponseResultsIT.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsIT.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_it_dict = tv_series_watch_providers200_response_results_it_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsIT from a dict
tv_series_watch_providers200_response_results_it_from_dict = TvSeriesWatchProviders200ResponseResultsIT.from_dict(tv_series_watch_providers200_response_results_it_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



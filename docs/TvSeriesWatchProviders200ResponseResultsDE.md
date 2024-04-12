# TvSeriesWatchProviders200ResponseResultsDE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsDEBuyInner]**](MovieWatchProviders200ResponseResultsDEBuyInner.md) |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsDEFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsDEFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_de import TvSeriesWatchProviders200ResponseResultsDE

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsDE from a JSON string
tv_series_watch_providers200_response_results_de_instance = TvSeriesWatchProviders200ResponseResultsDE.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsDE.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_de_dict = tv_series_watch_providers200_response_results_de_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsDE from a dict
tv_series_watch_providers200_response_results_de_from_dict = TvSeriesWatchProviders200ResponseResultsDE.from_dict(tv_series_watch_providers200_response_results_de_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



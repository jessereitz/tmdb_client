# TvSeriesWatchProviders200ResponseResultsGB


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsGBFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsGBFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsGBBuyInner]**](MovieWatchProviders200ResponseResultsGBBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_gb import TvSeriesWatchProviders200ResponseResultsGB

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsGB from a JSON string
tv_series_watch_providers200_response_results_gb_instance = TvSeriesWatchProviders200ResponseResultsGB.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsGB.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_gb_dict = tv_series_watch_providers200_response_results_gb_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsGB from a dict
tv_series_watch_providers200_response_results_gb_from_dict = TvSeriesWatchProviders200ResponseResultsGB.from_dict(tv_series_watch_providers200_response_results_gb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



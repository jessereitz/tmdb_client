# TvSeriesWatchProviders200ResponseResultsKR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsKRBuyInner]**](MovieWatchProviders200ResponseResultsKRBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_kr import TvSeriesWatchProviders200ResponseResultsKR

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsKR from a JSON string
tv_series_watch_providers200_response_results_kr_instance = TvSeriesWatchProviders200ResponseResultsKR.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsKR.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_kr_dict = tv_series_watch_providers200_response_results_kr_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsKR from a dict
tv_series_watch_providers200_response_results_kr_from_dict = TvSeriesWatchProviders200ResponseResultsKR.from_dict(tv_series_watch_providers200_response_results_kr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



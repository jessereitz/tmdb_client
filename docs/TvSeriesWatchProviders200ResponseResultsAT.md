# TvSeriesWatchProviders200ResponseResultsAT


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsATBuyInner]**](MovieWatchProviders200ResponseResultsATBuyInner.md) |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsATFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsATFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_series_watch_providers200_response_results_at import TvSeriesWatchProviders200ResponseResultsAT

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsAT from a JSON string
tv_series_watch_providers200_response_results_at_instance = TvSeriesWatchProviders200ResponseResultsAT.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsAT.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_at_dict = tv_series_watch_providers200_response_results_at_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsAT from a dict
tv_series_watch_providers200_response_results_at_from_dict = TvSeriesWatchProviders200ResponseResultsAT.from_dict(tv_series_watch_providers200_response_results_at_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



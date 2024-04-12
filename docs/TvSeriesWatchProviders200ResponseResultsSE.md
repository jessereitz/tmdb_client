# TvSeriesWatchProviders200ResponseResultsSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsCRFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsCRFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsSEBuyInner]**](MovieWatchProviders200ResponseResultsSEBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_se import TvSeriesWatchProviders200ResponseResultsSE

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsSE from a JSON string
tv_series_watch_providers200_response_results_se_instance = TvSeriesWatchProviders200ResponseResultsSE.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsSE.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_se_dict = tv_series_watch_providers200_response_results_se_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsSE from a dict
tv_series_watch_providers200_response_results_se_from_dict = TvSeriesWatchProviders200ResponseResultsSE.from_dict(tv_series_watch_providers200_response_results_se_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



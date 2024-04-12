# TvSeriesWatchProviders200ResponseResultsPL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsPLFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsPLFlatrateInner.md) |  | [optional] 
**rent** | [**List[TvSeriesWatchProviders200ResponseResultsPLRentInner]**](TvSeriesWatchProviders200ResponseResultsPLRentInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_series_watch_providers200_response_results_pl import TvSeriesWatchProviders200ResponseResultsPL

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsPL from a JSON string
tv_series_watch_providers200_response_results_pl_instance = TvSeriesWatchProviders200ResponseResultsPL.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsPL.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_pl_dict = tv_series_watch_providers200_response_results_pl_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsPL from a dict
tv_series_watch_providers200_response_results_pl_from_dict = TvSeriesWatchProviders200ResponseResultsPL.from_dict(tv_series_watch_providers200_response_results_pl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



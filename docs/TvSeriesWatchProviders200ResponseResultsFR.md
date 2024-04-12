# TvSeriesWatchProviders200ResponseResultsFR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsFRRentInner]**](MovieWatchProviders200ResponseResultsFRRentInner.md) |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsFRFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsFRFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_series_watch_providers200_response_results_fr import TvSeriesWatchProviders200ResponseResultsFR

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsFR from a JSON string
tv_series_watch_providers200_response_results_fr_instance = TvSeriesWatchProviders200ResponseResultsFR.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsFR.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_fr_dict = tv_series_watch_providers200_response_results_fr_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsFR from a dict
tv_series_watch_providers200_response_results_fr_from_dict = TvSeriesWatchProviders200ResponseResultsFR.from_dict(tv_series_watch_providers200_response_results_fr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



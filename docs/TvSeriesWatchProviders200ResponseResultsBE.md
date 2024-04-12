# TvSeriesWatchProviders200ResponseResultsBE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsBEFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsBEFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_series_watch_providers200_response_results_be import TvSeriesWatchProviders200ResponseResultsBE

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsBE from a JSON string
tv_series_watch_providers200_response_results_be_instance = TvSeriesWatchProviders200ResponseResultsBE.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsBE.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_be_dict = tv_series_watch_providers200_response_results_be_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsBE from a dict
tv_series_watch_providers200_response_results_be_from_dict = TvSeriesWatchProviders200ResponseResultsBE.from_dict(tv_series_watch_providers200_response_results_be_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



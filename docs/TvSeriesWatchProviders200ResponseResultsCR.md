# TvSeriesWatchProviders200ResponseResultsCR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsCRFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsCRFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_series_watch_providers200_response_results_cr import TvSeriesWatchProviders200ResponseResultsCR

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsCR from a JSON string
tv_series_watch_providers200_response_results_cr_instance = TvSeriesWatchProviders200ResponseResultsCR.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsCR.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_cr_dict = tv_series_watch_providers200_response_results_cr_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsCR from a dict
tv_series_watch_providers200_response_results_cr_from_dict = TvSeriesWatchProviders200ResponseResultsCR.from_dict(tv_series_watch_providers200_response_results_cr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



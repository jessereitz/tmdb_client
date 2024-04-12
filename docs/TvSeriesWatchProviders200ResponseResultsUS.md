# TvSeriesWatchProviders200ResponseResultsUS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**free** | [**List[TvSeriesWatchProviders200ResponseResultsBRFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsBRFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsDEBuyInner]**](MovieWatchProviders200ResponseResultsDEBuyInner.md) |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsBRFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsBRFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_series_watch_providers200_response_results_us import TvSeriesWatchProviders200ResponseResultsUS

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsUS from a JSON string
tv_series_watch_providers200_response_results_us_instance = TvSeriesWatchProviders200ResponseResultsUS.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsUS.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_us_dict = tv_series_watch_providers200_response_results_us_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsUS from a dict
tv_series_watch_providers200_response_results_us_from_dict = TvSeriesWatchProviders200ResponseResultsUS.from_dict(tv_series_watch_providers200_response_results_us_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



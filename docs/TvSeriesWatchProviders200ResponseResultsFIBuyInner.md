# TvSeriesWatchProviders200ResponseResultsFIBuyInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo_path** | **str** |  | [optional] 
**provider_id** | **int** |  | [optional] [default to 0]
**provider_name** | **str** |  | [optional] 
**display_priority** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_fi_buy_inner import TvSeriesWatchProviders200ResponseResultsFIBuyInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsFIBuyInner from a JSON string
tv_series_watch_providers200_response_results_fi_buy_inner_instance = TvSeriesWatchProviders200ResponseResultsFIBuyInner.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsFIBuyInner.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_fi_buy_inner_dict = tv_series_watch_providers200_response_results_fi_buy_inner_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsFIBuyInner from a dict
tv_series_watch_providers200_response_results_fi_buy_inner_from_dict = TvSeriesWatchProviders200ResponseResultsFIBuyInner.from_dict(tv_series_watch_providers200_response_results_fi_buy_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TvSeriesWatchProviders200ResponseResultsPLRentInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo_path** | **str** |  | [optional] 
**provider_id** | **int** |  | [optional] [default to 0]
**provider_name** | **str** |  | [optional] 
**display_priority** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_pl_rent_inner import TvSeriesWatchProviders200ResponseResultsPLRentInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsPLRentInner from a JSON string
tv_series_watch_providers200_response_results_pl_rent_inner_instance = TvSeriesWatchProviders200ResponseResultsPLRentInner.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsPLRentInner.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_pl_rent_inner_dict = tv_series_watch_providers200_response_results_pl_rent_inner_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsPLRentInner from a dict
tv_series_watch_providers200_response_results_pl_rent_inner_from_dict = TvSeriesWatchProviders200ResponseResultsPLRentInner.from_dict(tv_series_watch_providers200_response_results_pl_rent_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TvSeriesWatchProviders200ResponseResultsPE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsPEFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsPEFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_pe import TvSeriesWatchProviders200ResponseResultsPE

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsPE from a JSON string
tv_series_watch_providers200_response_results_pe_instance = TvSeriesWatchProviders200ResponseResultsPE.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsPE.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_pe_dict = tv_series_watch_providers200_response_results_pe_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsPE from a dict
tv_series_watch_providers200_response_results_pe_from_dict = TvSeriesWatchProviders200ResponseResultsPE.from_dict(tv_series_watch_providers200_response_results_pe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



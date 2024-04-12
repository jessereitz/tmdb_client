# TvSeriesWatchProviders200ResponseResultsCA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsBERentInner]**](MovieWatchProviders200ResponseResultsBERentInner.md) |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsCAFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsCAFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_ca import TvSeriesWatchProviders200ResponseResultsCA

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsCA from a JSON string
tv_series_watch_providers200_response_results_ca_instance = TvSeriesWatchProviders200ResponseResultsCA.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsCA.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_ca_dict = tv_series_watch_providers200_response_results_ca_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsCA from a dict
tv_series_watch_providers200_response_results_ca_from_dict = TvSeriesWatchProviders200ResponseResultsCA.from_dict(tv_series_watch_providers200_response_results_ca_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



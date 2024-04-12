# TvSeriesWatchProviders200ResponseResultsPA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsJMFlatrateInner]**](MovieWatchProviders200ResponseResultsJMFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_pa import TvSeriesWatchProviders200ResponseResultsPA

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsPA from a JSON string
tv_series_watch_providers200_response_results_pa_instance = TvSeriesWatchProviders200ResponseResultsPA.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsPA.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_pa_dict = tv_series_watch_providers200_response_results_pa_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsPA from a dict
tv_series_watch_providers200_response_results_pa_from_dict = TvSeriesWatchProviders200ResponseResultsPA.from_dict(tv_series_watch_providers200_response_results_pa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TvSeriesWatchProviders200ResponseResultsJM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsJMFlatrateInner]**](MovieWatchProviders200ResponseResultsJMFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_jm import TvSeriesWatchProviders200ResponseResultsJM

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsJM from a JSON string
tv_series_watch_providers200_response_results_jm_instance = TvSeriesWatchProviders200ResponseResultsJM.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsJM.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_jm_dict = tv_series_watch_providers200_response_results_jm_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsJM from a dict
tv_series_watch_providers200_response_results_jm_from_dict = TvSeriesWatchProviders200ResponseResultsJM.from_dict(tv_series_watch_providers200_response_results_jm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



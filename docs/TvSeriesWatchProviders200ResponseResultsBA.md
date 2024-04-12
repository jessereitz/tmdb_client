# TvSeriesWatchProviders200ResponseResultsBA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsBBFlatrateInner]**](MovieWatchProviders200ResponseResultsBBFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_ba import TvSeriesWatchProviders200ResponseResultsBA

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsBA from a JSON string
tv_series_watch_providers200_response_results_ba_instance = TvSeriesWatchProviders200ResponseResultsBA.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsBA.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_ba_dict = tv_series_watch_providers200_response_results_ba_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsBA from a dict
tv_series_watch_providers200_response_results_ba_from_dict = TvSeriesWatchProviders200ResponseResultsBA.from_dict(tv_series_watch_providers200_response_results_ba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TvSeriesWatchProviders200ResponseResultsBO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsBOFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsBOFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_bo import TvSeriesWatchProviders200ResponseResultsBO

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsBO from a JSON string
tv_series_watch_providers200_response_results_bo_instance = TvSeriesWatchProviders200ResponseResultsBO.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsBO.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_bo_dict = tv_series_watch_providers200_response_results_bo_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsBO from a dict
tv_series_watch_providers200_response_results_bo_from_dict = TvSeriesWatchProviders200ResponseResultsBO.from_dict(tv_series_watch_providers200_response_results_bo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



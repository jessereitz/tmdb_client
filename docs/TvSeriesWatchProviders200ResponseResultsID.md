# TvSeriesWatchProviders200ResponseResultsID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsIDFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsIDFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_id import TvSeriesWatchProviders200ResponseResultsID

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsID from a JSON string
tv_series_watch_providers200_response_results_id_instance = TvSeriesWatchProviders200ResponseResultsID.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsID.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_id_dict = tv_series_watch_providers200_response_results_id_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsID from a dict
tv_series_watch_providers200_response_results_id_from_dict = TvSeriesWatchProviders200ResponseResultsID.from_dict(tv_series_watch_providers200_response_results_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



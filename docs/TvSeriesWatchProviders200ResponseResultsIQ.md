# TvSeriesWatchProviders200ResponseResultsIQ


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsIQFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsIQFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_iq import TvSeriesWatchProviders200ResponseResultsIQ

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsIQ from a JSON string
tv_series_watch_providers200_response_results_iq_instance = TvSeriesWatchProviders200ResponseResultsIQ.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsIQ.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_iq_dict = tv_series_watch_providers200_response_results_iq_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsIQ from a dict
tv_series_watch_providers200_response_results_iq_from_dict = TvSeriesWatchProviders200ResponseResultsIQ.from_dict(tv_series_watch_providers200_response_results_iq_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



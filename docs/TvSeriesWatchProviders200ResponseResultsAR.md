# TvSeriesWatchProviders200ResponseResultsAR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsARFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsARFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_ar import TvSeriesWatchProviders200ResponseResultsAR

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsAR from a JSON string
tv_series_watch_providers200_response_results_ar_instance = TvSeriesWatchProviders200ResponseResultsAR.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsAR.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_ar_dict = tv_series_watch_providers200_response_results_ar_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsAR from a dict
tv_series_watch_providers200_response_results_ar_from_dict = TvSeriesWatchProviders200ResponseResultsAR.from_dict(tv_series_watch_providers200_response_results_ar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



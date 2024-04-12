# TvSeriesWatchProviders200ResponseResultsEC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsECFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsECFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_ec import TvSeriesWatchProviders200ResponseResultsEC

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsEC from a JSON string
tv_series_watch_providers200_response_results_ec_instance = TvSeriesWatchProviders200ResponseResultsEC.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsEC.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_ec_dict = tv_series_watch_providers200_response_results_ec_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsEC from a dict
tv_series_watch_providers200_response_results_ec_from_dict = TvSeriesWatchProviders200ResponseResultsEC.from_dict(tv_series_watch_providers200_response_results_ec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



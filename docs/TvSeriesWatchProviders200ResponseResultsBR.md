# TvSeriesWatchProviders200ResponseResultsBR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsBRFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsBRFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_br import TvSeriesWatchProviders200ResponseResultsBR

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsBR from a JSON string
tv_series_watch_providers200_response_results_br_instance = TvSeriesWatchProviders200ResponseResultsBR.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsBR.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_br_dict = tv_series_watch_providers200_response_results_br_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsBR from a dict
tv_series_watch_providers200_response_results_br_from_dict = TvSeriesWatchProviders200ResponseResultsBR.from_dict(tv_series_watch_providers200_response_results_br_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



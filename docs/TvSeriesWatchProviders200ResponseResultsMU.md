# TvSeriesWatchProviders200ResponseResultsMU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsMUFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsMUFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_watch_providers200_response_results_mu import TvSeriesWatchProviders200ResponseResultsMU

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesWatchProviders200ResponseResultsMU from a JSON string
tv_series_watch_providers200_response_results_mu_instance = TvSeriesWatchProviders200ResponseResultsMU.from_json(json)
# print the JSON string representation of the object
print(TvSeriesWatchProviders200ResponseResultsMU.to_json())

# convert the object into a dict
tv_series_watch_providers200_response_results_mu_dict = tv_series_watch_providers200_response_results_mu_instance.to_dict()
# create an instance of TvSeriesWatchProviders200ResponseResultsMU from a dict
tv_series_watch_providers200_response_results_mu_from_dict = TvSeriesWatchProviders200ResponseResultsMU.from_dict(tv_series_watch_providers200_response_results_mu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



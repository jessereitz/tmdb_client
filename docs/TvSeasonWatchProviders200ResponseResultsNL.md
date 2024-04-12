# TvSeasonWatchProviders200ResponseResultsNL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[TvSeriesWatchProviders200ResponseResultsFIBuyInner]**](TvSeriesWatchProviders200ResponseResultsFIBuyInner.md) |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsNLFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsNLFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_season_watch_providers200_response_results_nl import TvSeasonWatchProviders200ResponseResultsNL

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsNL from a JSON string
tv_season_watch_providers200_response_results_nl_instance = TvSeasonWatchProviders200ResponseResultsNL.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsNL.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_nl_dict = tv_season_watch_providers200_response_results_nl_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsNL from a dict
tv_season_watch_providers200_response_results_nl_from_dict = TvSeasonWatchProviders200ResponseResultsNL.from_dict(tv_season_watch_providers200_response_results_nl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


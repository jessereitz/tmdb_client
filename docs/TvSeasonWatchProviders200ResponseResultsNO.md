# TvSeasonWatchProviders200ResponseResultsNO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[TvSeriesWatchProviders200ResponseResultsNOBuyInner]**](TvSeriesWatchProviders200ResponseResultsNOBuyInner.md) |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsARFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsARFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_season_watch_providers200_response_results_no import TvSeasonWatchProviders200ResponseResultsNO

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsNO from a JSON string
tv_season_watch_providers200_response_results_no_instance = TvSeasonWatchProviders200ResponseResultsNO.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsNO.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_no_dict = tv_season_watch_providers200_response_results_no_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsNO from a dict
tv_season_watch_providers200_response_results_no_from_dict = TvSeasonWatchProviders200ResponseResultsNO.from_dict(tv_season_watch_providers200_response_results_no_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TvSeasonWatchProviders200ResponseResultsIE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[TvSeriesWatchProviders200ResponseResultsIEBuyInner]**](TvSeriesWatchProviders200ResponseResultsIEBuyInner.md) |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsIEFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsIEFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_ie import TvSeasonWatchProviders200ResponseResultsIE

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsIE from a JSON string
tv_season_watch_providers200_response_results_ie_instance = TvSeasonWatchProviders200ResponseResultsIE.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsIE.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_ie_dict = tv_season_watch_providers200_response_results_ie_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsIE from a dict
tv_season_watch_providers200_response_results_ie_from_dict = TvSeasonWatchProviders200ResponseResultsIE.from_dict(tv_season_watch_providers200_response_results_ie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TvSeasonWatchProviders200ResponseResultsJP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[TvSeriesWatchProviders200ResponseResultsJPBuyInner]**](TvSeriesWatchProviders200ResponseResultsJPBuyInner.md) |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsJPFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsJPFlatrateInner.md) |  | [optional] 
**rent** | [**List[TvSeriesWatchProviders200ResponseResultsJPBuyInner]**](TvSeriesWatchProviders200ResponseResultsJPBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_jp import TvSeasonWatchProviders200ResponseResultsJP

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsJP from a JSON string
tv_season_watch_providers200_response_results_jp_instance = TvSeasonWatchProviders200ResponseResultsJP.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsJP.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_jp_dict = tv_season_watch_providers200_response_results_jp_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsJP from a dict
tv_season_watch_providers200_response_results_jp_from_dict = TvSeasonWatchProviders200ResponseResultsJP.from_dict(tv_season_watch_providers200_response_results_jp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



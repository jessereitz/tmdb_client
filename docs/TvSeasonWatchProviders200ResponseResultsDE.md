# TvSeasonWatchProviders200ResponseResultsDE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsDEBuyInner]**](MovieWatchProviders200ResponseResultsDEBuyInner.md) |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsDEFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsDEFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_de import TvSeasonWatchProviders200ResponseResultsDE

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsDE from a JSON string
tv_season_watch_providers200_response_results_de_instance = TvSeasonWatchProviders200ResponseResultsDE.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsDE.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_de_dict = tv_season_watch_providers200_response_results_de_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsDE from a dict
tv_season_watch_providers200_response_results_de_from_dict = TvSeasonWatchProviders200ResponseResultsDE.from_dict(tv_season_watch_providers200_response_results_de_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TvSeasonWatchProviders200ResponseResultsRU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsRUFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsRUFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_ru import TvSeasonWatchProviders200ResponseResultsRU

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsRU from a JSON string
tv_season_watch_providers200_response_results_ru_instance = TvSeasonWatchProviders200ResponseResultsRU.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsRU.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_ru_dict = tv_season_watch_providers200_response_results_ru_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsRU from a dict
tv_season_watch_providers200_response_results_ru_from_dict = TvSeasonWatchProviders200ResponseResultsRU.from_dict(tv_season_watch_providers200_response_results_ru_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



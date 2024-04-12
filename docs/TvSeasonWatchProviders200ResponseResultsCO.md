# TvSeasonWatchProviders200ResponseResultsCO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsCOFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsCOFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_co import TvSeasonWatchProviders200ResponseResultsCO

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsCO from a JSON string
tv_season_watch_providers200_response_results_co_instance = TvSeasonWatchProviders200ResponseResultsCO.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsCO.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_co_dict = tv_season_watch_providers200_response_results_co_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsCO from a dict
tv_season_watch_providers200_response_results_co_from_dict = TvSeasonWatchProviders200ResponseResultsCO.from_dict(tv_season_watch_providers200_response_results_co_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



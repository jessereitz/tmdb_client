# TvSeasonWatchProviders200ResponseResultsRO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsROFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsROFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_ro import TvSeasonWatchProviders200ResponseResultsRO

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsRO from a JSON string
tv_season_watch_providers200_response_results_ro_instance = TvSeasonWatchProviders200ResponseResultsRO.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsRO.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_ro_dict = tv_season_watch_providers200_response_results_ro_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsRO from a dict
tv_season_watch_providers200_response_results_ro_from_dict = TvSeasonWatchProviders200ResponseResultsRO.from_dict(tv_season_watch_providers200_response_results_ro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



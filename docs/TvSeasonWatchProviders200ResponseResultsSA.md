# TvSeasonWatchProviders200ResponseResultsSA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsSAFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsSAFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_sa import TvSeasonWatchProviders200ResponseResultsSA

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsSA from a JSON string
tv_season_watch_providers200_response_results_sa_instance = TvSeasonWatchProviders200ResponseResultsSA.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsSA.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_sa_dict = tv_season_watch_providers200_response_results_sa_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsSA from a dict
tv_season_watch_providers200_response_results_sa_from_dict = TvSeasonWatchProviders200ResponseResultsSA.from_dict(tv_season_watch_providers200_response_results_sa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



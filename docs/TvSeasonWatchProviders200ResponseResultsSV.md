# TvSeasonWatchProviders200ResponseResultsSV


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsSVFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsSVFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_sv import TvSeasonWatchProviders200ResponseResultsSV

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsSV from a JSON string
tv_season_watch_providers200_response_results_sv_instance = TvSeasonWatchProviders200ResponseResultsSV.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsSV.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_sv_dict = tv_season_watch_providers200_response_results_sv_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsSV from a dict
tv_season_watch_providers200_response_results_sv_from_dict = TvSeasonWatchProviders200ResponseResultsSV.from_dict(tv_season_watch_providers200_response_results_sv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



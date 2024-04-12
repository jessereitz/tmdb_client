# TvSeasonWatchProviders200ResponseResultsVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsPEFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsPEFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_ve import TvSeasonWatchProviders200ResponseResultsVE

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsVE from a JSON string
tv_season_watch_providers200_response_results_ve_instance = TvSeasonWatchProviders200ResponseResultsVE.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsVE.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_ve_dict = tv_season_watch_providers200_response_results_ve_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsVE from a dict
tv_season_watch_providers200_response_results_ve_from_dict = TvSeasonWatchProviders200ResponseResultsVE.from_dict(tv_season_watch_providers200_response_results_ve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



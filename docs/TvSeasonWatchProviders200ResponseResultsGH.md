# TvSeasonWatchProviders200ResponseResultsGH


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsGHFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsGHFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_gh import TvSeasonWatchProviders200ResponseResultsGH

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsGH from a JSON string
tv_season_watch_providers200_response_results_gh_instance = TvSeasonWatchProviders200ResponseResultsGH.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsGH.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_gh_dict = tv_season_watch_providers200_response_results_gh_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsGH from a dict
tv_season_watch_providers200_response_results_gh_from_dict = TvSeasonWatchProviders200ResponseResultsGH.from_dict(tv_season_watch_providers200_response_results_gh_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



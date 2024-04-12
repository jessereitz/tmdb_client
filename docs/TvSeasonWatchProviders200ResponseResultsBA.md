# TvSeasonWatchProviders200ResponseResultsBA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsBBFlatrateInner]**](MovieWatchProviders200ResponseResultsBBFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_ba import TvSeasonWatchProviders200ResponseResultsBA

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsBA from a JSON string
tv_season_watch_providers200_response_results_ba_instance = TvSeasonWatchProviders200ResponseResultsBA.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsBA.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_ba_dict = tv_season_watch_providers200_response_results_ba_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsBA from a dict
tv_season_watch_providers200_response_results_ba_from_dict = TvSeasonWatchProviders200ResponseResultsBA.from_dict(tv_season_watch_providers200_response_results_ba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



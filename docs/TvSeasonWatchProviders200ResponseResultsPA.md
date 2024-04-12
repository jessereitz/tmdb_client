# TvSeasonWatchProviders200ResponseResultsPA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsJMFlatrateInner]**](MovieWatchProviders200ResponseResultsJMFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_pa import TvSeasonWatchProviders200ResponseResultsPA

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsPA from a JSON string
tv_season_watch_providers200_response_results_pa_instance = TvSeasonWatchProviders200ResponseResultsPA.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsPA.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_pa_dict = tv_season_watch_providers200_response_results_pa_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsPA from a dict
tv_season_watch_providers200_response_results_pa_from_dict = TvSeasonWatchProviders200ResponseResultsPA.from_dict(tv_season_watch_providers200_response_results_pa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



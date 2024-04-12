# TvSeasonWatchProviders200ResponseResultsDO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsBBFlatrateInner]**](MovieWatchProviders200ResponseResultsBBFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_do import TvSeasonWatchProviders200ResponseResultsDO

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsDO from a JSON string
tv_season_watch_providers200_response_results_do_instance = TvSeasonWatchProviders200ResponseResultsDO.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsDO.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_do_dict = tv_season_watch_providers200_response_results_do_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsDO from a dict
tv_season_watch_providers200_response_results_do_from_dict = TvSeasonWatchProviders200ResponseResultsDO.from_dict(tv_season_watch_providers200_response_results_do_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TvSeasonWatchProviders200ResponseResultsSC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsSCFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsSCFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_sc import TvSeasonWatchProviders200ResponseResultsSC

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsSC from a JSON string
tv_season_watch_providers200_response_results_sc_instance = TvSeasonWatchProviders200ResponseResultsSC.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsSC.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_sc_dict = tv_season_watch_providers200_response_results_sc_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsSC from a dict
tv_season_watch_providers200_response_results_sc_from_dict = TvSeasonWatchProviders200ResponseResultsSC.from_dict(tv_season_watch_providers200_response_results_sc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



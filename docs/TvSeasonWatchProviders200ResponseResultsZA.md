# TvSeasonWatchProviders200ResponseResultsZA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsZAFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsZAFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_za import TvSeasonWatchProviders200ResponseResultsZA

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsZA from a JSON string
tv_season_watch_providers200_response_results_za_instance = TvSeasonWatchProviders200ResponseResultsZA.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsZA.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_za_dict = tv_season_watch_providers200_response_results_za_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsZA from a dict
tv_season_watch_providers200_response_results_za_from_dict = TvSeasonWatchProviders200ResponseResultsZA.from_dict(tv_season_watch_providers200_response_results_za_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



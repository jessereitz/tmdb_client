# TvSeasonWatchProviders200ResponseResultsRS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsRSFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsRSFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_rs import TvSeasonWatchProviders200ResponseResultsRS

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsRS from a JSON string
tv_season_watch_providers200_response_results_rs_instance = TvSeasonWatchProviders200ResponseResultsRS.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsRS.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_rs_dict = tv_season_watch_providers200_response_results_rs_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsRS from a dict
tv_season_watch_providers200_response_results_rs_from_dict = TvSeasonWatchProviders200ResponseResultsRS.from_dict(tv_season_watch_providers200_response_results_rs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



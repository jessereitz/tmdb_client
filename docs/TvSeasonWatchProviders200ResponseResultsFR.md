# TvSeasonWatchProviders200ResponseResultsFR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsFRFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsFRFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsFRRentInner]**](MovieWatchProviders200ResponseResultsFRRentInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_fr import TvSeasonWatchProviders200ResponseResultsFR

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsFR from a JSON string
tv_season_watch_providers200_response_results_fr_instance = TvSeasonWatchProviders200ResponseResultsFR.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsFR.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_fr_dict = tv_season_watch_providers200_response_results_fr_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsFR from a dict
tv_season_watch_providers200_response_results_fr_from_dict = TvSeasonWatchProviders200ResponseResultsFR.from_dict(tv_season_watch_providers200_response_results_fr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



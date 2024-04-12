# TvSeasonWatchProviders200ResponseResultsFI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsCRFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsCRFlatrateInner.md) |  | [optional] 
**buy** | [**List[TvSeriesWatchProviders200ResponseResultsFIBuyInner]**](TvSeriesWatchProviders200ResponseResultsFIBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_fi import TvSeasonWatchProviders200ResponseResultsFI

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsFI from a JSON string
tv_season_watch_providers200_response_results_fi_instance = TvSeasonWatchProviders200ResponseResultsFI.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsFI.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_fi_dict = tv_season_watch_providers200_response_results_fi_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsFI from a dict
tv_season_watch_providers200_response_results_fi_from_dict = TvSeasonWatchProviders200ResponseResultsFI.from_dict(tv_season_watch_providers200_response_results_fi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TvSeasonWatchProviders200ResponseResultsSG


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsSGFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsSGFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_sg import TvSeasonWatchProviders200ResponseResultsSG

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsSG from a JSON string
tv_season_watch_providers200_response_results_sg_instance = TvSeasonWatchProviders200ResponseResultsSG.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsSG.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_sg_dict = tv_season_watch_providers200_response_results_sg_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsSG from a dict
tv_season_watch_providers200_response_results_sg_from_dict = TvSeasonWatchProviders200ResponseResultsSG.from_dict(tv_season_watch_providers200_response_results_sg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



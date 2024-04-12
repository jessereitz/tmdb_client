# TvSeasonWatchProviders200ResponseResultsTR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsTRFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsTRFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_tr import TvSeasonWatchProviders200ResponseResultsTR

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsTR from a JSON string
tv_season_watch_providers200_response_results_tr_instance = TvSeasonWatchProviders200ResponseResultsTR.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsTR.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_tr_dict = tv_season_watch_providers200_response_results_tr_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsTR from a dict
tv_season_watch_providers200_response_results_tr_from_dict = TvSeasonWatchProviders200ResponseResultsTR.from_dict(tv_season_watch_providers200_response_results_tr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



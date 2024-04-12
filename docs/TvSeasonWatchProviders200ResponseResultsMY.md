# TvSeasonWatchProviders200ResponseResultsMY


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsIDFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsIDFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_my import TvSeasonWatchProviders200ResponseResultsMY

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsMY from a JSON string
tv_season_watch_providers200_response_results_my_instance = TvSeasonWatchProviders200ResponseResultsMY.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsMY.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_my_dict = tv_season_watch_providers200_response_results_my_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsMY from a dict
tv_season_watch_providers200_response_results_my_from_dict = TvSeasonWatchProviders200ResponseResultsMY.from_dict(tv_season_watch_providers200_response_results_my_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



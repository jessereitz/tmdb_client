# TvSeasonWatchProviders200ResponseResultsNG


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsDZFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsDZFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_ng import TvSeasonWatchProviders200ResponseResultsNG

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsNG from a JSON string
tv_season_watch_providers200_response_results_ng_instance = TvSeasonWatchProviders200ResponseResultsNG.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsNG.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_ng_dict = tv_season_watch_providers200_response_results_ng_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsNG from a dict
tv_season_watch_providers200_response_results_ng_from_dict = TvSeasonWatchProviders200ResponseResultsNG.from_dict(tv_season_watch_providers200_response_results_ng_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



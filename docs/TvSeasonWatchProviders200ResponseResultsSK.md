# TvSeasonWatchProviders200ResponseResultsSK


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsSKFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsSKFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_sk import TvSeasonWatchProviders200ResponseResultsSK

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsSK from a JSON string
tv_season_watch_providers200_response_results_sk_instance = TvSeasonWatchProviders200ResponseResultsSK.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsSK.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_sk_dict = tv_season_watch_providers200_response_results_sk_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsSK from a dict
tv_season_watch_providers200_response_results_sk_from_dict = TvSeasonWatchProviders200ResponseResultsSK.from_dict(tv_season_watch_providers200_response_results_sk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



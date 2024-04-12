# TvSeasonWatchProviders200ResponseResultsPL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**rent** | [**List[TvSeriesWatchProviders200ResponseResultsPLRentInner]**](TvSeriesWatchProviders200ResponseResultsPLRentInner.md) |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsPLFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsPLFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_season_watch_providers200_response_results_pl import TvSeasonWatchProviders200ResponseResultsPL

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsPL from a JSON string
tv_season_watch_providers200_response_results_pl_instance = TvSeasonWatchProviders200ResponseResultsPL.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsPL.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_pl_dict = tv_season_watch_providers200_response_results_pl_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsPL from a dict
tv_season_watch_providers200_response_results_pl_from_dict = TvSeasonWatchProviders200ResponseResultsPL.from_dict(tv_season_watch_providers200_response_results_pl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



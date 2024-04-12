# TvSeasonWatchProviders200ResponseResultsPE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsPEFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsPEFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_pe import TvSeasonWatchProviders200ResponseResultsPE

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsPE from a JSON string
tv_season_watch_providers200_response_results_pe_instance = TvSeasonWatchProviders200ResponseResultsPE.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsPE.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_pe_dict = tv_season_watch_providers200_response_results_pe_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsPE from a dict
tv_season_watch_providers200_response_results_pe_from_dict = TvSeasonWatchProviders200ResponseResultsPE.from_dict(tv_season_watch_providers200_response_results_pe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TvSeasonWatchProviders200ResponseResultsAU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsAUBuyInner]**](MovieWatchProviders200ResponseResultsAUBuyInner.md) |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsAUFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_season_watch_providers200_response_results_au import TvSeasonWatchProviders200ResponseResultsAU

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsAU from a JSON string
tv_season_watch_providers200_response_results_au_instance = TvSeasonWatchProviders200ResponseResultsAU.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsAU.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_au_dict = tv_season_watch_providers200_response_results_au_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsAU from a dict
tv_season_watch_providers200_response_results_au_from_dict = TvSeasonWatchProviders200ResponseResultsAU.from_dict(tv_season_watch_providers200_response_results_au_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



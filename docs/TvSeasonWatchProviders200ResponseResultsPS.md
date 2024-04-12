# TvSeasonWatchProviders200ResponseResultsPS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsIQFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsIQFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_season_watch_providers200_response_results_ps import TvSeasonWatchProviders200ResponseResultsPS

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsPS from a JSON string
tv_season_watch_providers200_response_results_ps_instance = TvSeasonWatchProviders200ResponseResultsPS.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsPS.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_ps_dict = tv_season_watch_providers200_response_results_ps_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsPS from a dict
tv_season_watch_providers200_response_results_ps_from_dict = TvSeasonWatchProviders200ResponseResultsPS.from_dict(tv_season_watch_providers200_response_results_ps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TvSeasonWatchProviders200ResponseResultsCA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsBERentInner]**](MovieWatchProviders200ResponseResultsBERentInner.md) |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsCAFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsCAFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_season_watch_providers200_response_results_ca import TvSeasonWatchProviders200ResponseResultsCA

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsCA from a JSON string
tv_season_watch_providers200_response_results_ca_instance = TvSeasonWatchProviders200ResponseResultsCA.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsCA.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_ca_dict = tv_season_watch_providers200_response_results_ca_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsCA from a dict
tv_season_watch_providers200_response_results_ca_from_dict = TvSeasonWatchProviders200ResponseResultsCA.from_dict(tv_season_watch_providers200_response_results_ca_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TvSeasonWatchProviders200ResponseResultsBE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsBEFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsBEFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_season_watch_providers200_response_results_be import TvSeasonWatchProviders200ResponseResultsBE

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsBE from a JSON string
tv_season_watch_providers200_response_results_be_instance = TvSeasonWatchProviders200ResponseResultsBE.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsBE.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_be_dict = tv_season_watch_providers200_response_results_be_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsBE from a dict
tv_season_watch_providers200_response_results_be_from_dict = TvSeasonWatchProviders200ResponseResultsBE.from_dict(tv_season_watch_providers200_response_results_be_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



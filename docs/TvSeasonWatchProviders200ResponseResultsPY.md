# TvSeasonWatchProviders200ResponseResultsPY


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsBOFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsBOFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_py import TvSeasonWatchProviders200ResponseResultsPY

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsPY from a JSON string
tv_season_watch_providers200_response_results_py_instance = TvSeasonWatchProviders200ResponseResultsPY.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsPY.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_py_dict = tv_season_watch_providers200_response_results_py_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsPY from a dict
tv_season_watch_providers200_response_results_py_from_dict = TvSeasonWatchProviders200ResponseResultsPY.from_dict(tv_season_watch_providers200_response_results_py_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



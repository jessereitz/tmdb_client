# TvSeasonWatchProviders200ResponseResultsCL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsBRFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsBRFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_cl import TvSeasonWatchProviders200ResponseResultsCL

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsCL from a JSON string
tv_season_watch_providers200_response_results_cl_instance = TvSeasonWatchProviders200ResponseResultsCL.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsCL.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_cl_dict = tv_season_watch_providers200_response_results_cl_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsCL from a dict
tv_season_watch_providers200_response_results_cl_from_dict = TvSeasonWatchProviders200ResponseResultsCL.from_dict(tv_season_watch_providers200_response_results_cl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



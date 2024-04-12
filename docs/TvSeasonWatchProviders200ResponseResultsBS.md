# TvSeasonWatchProviders200ResponseResultsBS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsBBFlatrateInner]**](MovieWatchProviders200ResponseResultsBBFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_bs import TvSeasonWatchProviders200ResponseResultsBS

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsBS from a JSON string
tv_season_watch_providers200_response_results_bs_instance = TvSeasonWatchProviders200ResponseResultsBS.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsBS.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_bs_dict = tv_season_watch_providers200_response_results_bs_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsBS from a dict
tv_season_watch_providers200_response_results_bs_from_dict = TvSeasonWatchProviders200ResponseResultsBS.from_dict(tv_season_watch_providers200_response_results_bs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TvSeasonWatchProviders200ResponseResultsHR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[TvSeriesWatchProviders200ResponseResultsHRFlatrateInner]**](TvSeriesWatchProviders200ResponseResultsHRFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_hr import TvSeasonWatchProviders200ResponseResultsHR

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsHR from a JSON string
tv_season_watch_providers200_response_results_hr_instance = TvSeasonWatchProviders200ResponseResultsHR.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsHR.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_hr_dict = tv_season_watch_providers200_response_results_hr_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsHR from a dict
tv_season_watch_providers200_response_results_hr_from_dict = TvSeasonWatchProviders200ResponseResultsHR.from_dict(tv_season_watch_providers200_response_results_hr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



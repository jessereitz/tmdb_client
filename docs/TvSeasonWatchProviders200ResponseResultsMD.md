# TvSeasonWatchProviders200ResponseResultsMD


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsMDFlatrateInner]**](MovieWatchProviders200ResponseResultsMDFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_watch_providers200_response_results_md import TvSeasonWatchProviders200ResponseResultsMD

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200ResponseResultsMD from a JSON string
tv_season_watch_providers200_response_results_md_instance = TvSeasonWatchProviders200ResponseResultsMD.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200ResponseResultsMD.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_results_md_dict = tv_season_watch_providers200_response_results_md_instance.to_dict()
# create an instance of TvSeasonWatchProviders200ResponseResultsMD from a dict
tv_season_watch_providers200_response_results_md_from_dict = TvSeasonWatchProviders200ResponseResultsMD.from_dict(tv_season_watch_providers200_response_results_md_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



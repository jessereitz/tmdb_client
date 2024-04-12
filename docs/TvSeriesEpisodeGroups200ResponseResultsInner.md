# TvSeriesEpisodeGroups200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**episode_count** | **int** |  | [optional] [default to 0]
**group_count** | **int** |  | [optional] [default to 0]
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**network** | [**TvSeriesDetails200ResponseNetworksInner**](TvSeriesDetails200ResponseNetworksInner.md) |  | [optional] 
**type** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.tv_series_episode_groups200_response_results_inner import TvSeriesEpisodeGroups200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesEpisodeGroups200ResponseResultsInner from a JSON string
tv_series_episode_groups200_response_results_inner_instance = TvSeriesEpisodeGroups200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(TvSeriesEpisodeGroups200ResponseResultsInner.to_json())

# convert the object into a dict
tv_series_episode_groups200_response_results_inner_dict = tv_series_episode_groups200_response_results_inner_instance.to_dict()
# create an instance of TvSeriesEpisodeGroups200ResponseResultsInner from a dict
tv_series_episode_groups200_response_results_inner_from_dict = TvSeriesEpisodeGroups200ResponseResultsInner.from_dict(tv_series_episode_groups200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TvSeasonVideos200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_639_1** | **str** |  | [optional] 
**iso_3166_1** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**site** | **str** |  | [optional] 
**size** | **int** |  | [optional] [default to 0]
**type** | **str** |  | [optional] 
**official** | **bool** |  | [optional] [default to True]
**published_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tv_season_videos200_response_results_inner import TvSeasonVideos200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonVideos200ResponseResultsInner from a JSON string
tv_season_videos200_response_results_inner_instance = TvSeasonVideos200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(TvSeasonVideos200ResponseResultsInner.to_json())

# convert the object into a dict
tv_season_videos200_response_results_inner_dict = tv_season_videos200_response_results_inner_instance.to_dict()
# create an instance of TvSeasonVideos200ResponseResultsInner from a dict
tv_season_videos200_response_results_inner_from_dict = TvSeasonVideos200ResponseResultsInner.from_dict(tv_season_videos200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



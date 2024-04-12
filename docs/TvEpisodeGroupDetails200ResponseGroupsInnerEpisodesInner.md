# TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**air_date** | **str** |  | [optional] 
**episode_number** | **int** |  | [optional] [default to 0]
**id** | **int** |  | [optional] [default to 0]
**name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**production_code** | **str** |  | [optional] 
**runtime** | **object** |  | [optional] 
**season_number** | **int** |  | [optional] [default to 0]
**show_id** | **int** |  | [optional] [default to 0]
**still_path** | **str** |  | [optional] 
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]
**order** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.tv_episode_group_details200_response_groups_inner_episodes_inner import TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner from a JSON string
tv_episode_group_details200_response_groups_inner_episodes_inner_instance = TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner.from_json(json)
# print the JSON string representation of the object
print(TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner.to_json())

# convert the object into a dict
tv_episode_group_details200_response_groups_inner_episodes_inner_dict = tv_episode_group_details200_response_groups_inner_episodes_inner_instance.to_dict()
# create an instance of TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner from a dict
tv_episode_group_details200_response_groups_inner_episodes_inner_from_dict = TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner.from_dict(tv_episode_group_details200_response_groups_inner_episodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TvEpisodeGroupDetails200ResponseGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**order** | **int** |  | [optional] [default to 0]
**episodes** | [**List[TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner]**](TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner.md) |  | [optional] 
**locked** | **bool** |  | [optional] [default to True]

## Example

```python
from openapi_client.models.tv_episode_group_details200_response_groups_inner import TvEpisodeGroupDetails200ResponseGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvEpisodeGroupDetails200ResponseGroupsInner from a JSON string
tv_episode_group_details200_response_groups_inner_instance = TvEpisodeGroupDetails200ResponseGroupsInner.from_json(json)
# print the JSON string representation of the object
print(TvEpisodeGroupDetails200ResponseGroupsInner.to_json())

# convert the object into a dict
tv_episode_group_details200_response_groups_inner_dict = tv_episode_group_details200_response_groups_inner_instance.to_dict()
# create an instance of TvEpisodeGroupDetails200ResponseGroupsInner from a dict
tv_episode_group_details200_response_groups_inner_from_dict = TvEpisodeGroupDetails200ResponseGroupsInner.from_dict(tv_episode_group_details200_response_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



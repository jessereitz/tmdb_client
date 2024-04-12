# TvEpisodeGroupDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**episode_count** | **int** |  | [optional] [default to 0]
**group_count** | **int** |  | [optional] [default to 0]
**groups** | [**List[TvEpisodeGroupDetails200ResponseGroupsInner]**](TvEpisodeGroupDetails200ResponseGroupsInner.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**network** | [**TvEpisodeGroupDetails200ResponseNetwork**](TvEpisodeGroupDetails200ResponseNetwork.md) |  | [optional] 
**type** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.tv_episode_group_details200_response import TvEpisodeGroupDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvEpisodeGroupDetails200Response from a JSON string
tv_episode_group_details200_response_instance = TvEpisodeGroupDetails200Response.from_json(json)
# print the JSON string representation of the object
print(TvEpisodeGroupDetails200Response.to_json())

# convert the object into a dict
tv_episode_group_details200_response_dict = tv_episode_group_details200_response_instance.to_dict()
# create an instance of TvEpisodeGroupDetails200Response from a dict
tv_episode_group_details200_response_from_dict = TvEpisodeGroupDetails200Response.from_dict(tv_episode_group_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



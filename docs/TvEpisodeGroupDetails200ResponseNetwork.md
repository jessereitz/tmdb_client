# TvEpisodeGroupDetails200ResponseNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**logo_path** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**origin_country** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.tv_episode_group_details200_response_network import TvEpisodeGroupDetails200ResponseNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of TvEpisodeGroupDetails200ResponseNetwork from a JSON string
tv_episode_group_details200_response_network_instance = TvEpisodeGroupDetails200ResponseNetwork.from_json(json)
# print the JSON string representation of the object
print(TvEpisodeGroupDetails200ResponseNetwork.to_json())

# convert the object into a dict
tv_episode_group_details200_response_network_dict = tv_episode_group_details200_response_network_instance.to_dict()
# create an instance of TvEpisodeGroupDetails200ResponseNetwork from a dict
tv_episode_group_details200_response_network_from_dict = TvEpisodeGroupDetails200ResponseNetwork.from_dict(tv_episode_group_details200_response_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



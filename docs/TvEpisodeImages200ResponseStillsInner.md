# TvEpisodeImages200ResponseStillsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_ratio** | **float** |  | [optional] [default to 0]
**height** | **int** |  | [optional] [default to 0]
**iso_639_1** | **object** |  | [optional] 
**file_path** | **str** |  | [optional] 
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]
**width** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.tv_episode_images200_response_stills_inner import TvEpisodeImages200ResponseStillsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvEpisodeImages200ResponseStillsInner from a JSON string
tv_episode_images200_response_stills_inner_instance = TvEpisodeImages200ResponseStillsInner.from_json(json)
# print the JSON string representation of the object
print(TvEpisodeImages200ResponseStillsInner.to_json())

# convert the object into a dict
tv_episode_images200_response_stills_inner_dict = tv_episode_images200_response_stills_inner_instance.to_dict()
# create an instance of TvEpisodeImages200ResponseStillsInner from a dict
tv_episode_images200_response_stills_inner_from_dict = TvEpisodeImages200ResponseStillsInner.from_dict(tv_episode_images200_response_stills_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



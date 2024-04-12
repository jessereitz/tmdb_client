# TvEpisodeImages200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**stills** | [**List[TvEpisodeImages200ResponseStillsInner]**](TvEpisodeImages200ResponseStillsInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_episode_images200_response import TvEpisodeImages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvEpisodeImages200Response from a JSON string
tv_episode_images200_response_instance = TvEpisodeImages200Response.from_json(json)
# print the JSON string representation of the object
print(TvEpisodeImages200Response.to_json())

# convert the object into a dict
tv_episode_images200_response_dict = tv_episode_images200_response_instance.to_dict()
# create an instance of TvEpisodeImages200Response from a dict
tv_episode_images200_response_from_dict = TvEpisodeImages200Response.from_dict(tv_episode_images200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



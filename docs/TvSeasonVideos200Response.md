# TvSeasonVideos200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**results** | [**List[TvSeasonVideos200ResponseResultsInner]**](TvSeasonVideos200ResponseResultsInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_videos200_response import TvSeasonVideos200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonVideos200Response from a JSON string
tv_season_videos200_response_instance = TvSeasonVideos200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeasonVideos200Response.to_json())

# convert the object into a dict
tv_season_videos200_response_dict = tv_season_videos200_response_instance.to_dict()
# create an instance of TvSeasonVideos200Response from a dict
tv_season_videos200_response_from_dict = TvSeasonVideos200Response.from_dict(tv_season_videos200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MovieVideos200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**results** | [**List[MovieVideos200ResponseResultsInner]**](MovieVideos200ResponseResultsInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_videos200_response import MovieVideos200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieVideos200Response from a JSON string
movie_videos200_response_instance = MovieVideos200Response.from_json(json)
# print the JSON string representation of the object
print(MovieVideos200Response.to_json())

# convert the object into a dict
movie_videos200_response_dict = movie_videos200_response_instance.to_dict()
# create an instance of MovieVideos200Response from a dict
movie_videos200_response_from_dict = MovieVideos200Response.from_dict(movie_videos200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



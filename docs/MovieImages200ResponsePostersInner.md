# MovieImages200ResponsePostersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_ratio** | **float** |  | [optional] [default to 0]
**height** | **int** |  | [optional] [default to 0]
**iso_639_1** | **str** |  | [optional] 
**file_path** | **str** |  | [optional] 
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]
**width** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.movie_images200_response_posters_inner import MovieImages200ResponsePostersInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieImages200ResponsePostersInner from a JSON string
movie_images200_response_posters_inner_instance = MovieImages200ResponsePostersInner.from_json(json)
# print the JSON string representation of the object
print(MovieImages200ResponsePostersInner.to_json())

# convert the object into a dict
movie_images200_response_posters_inner_dict = movie_images200_response_posters_inner_instance.to_dict()
# create an instance of MovieImages200ResponsePostersInner from a dict
movie_images200_response_posters_inner_from_dict = MovieImages200ResponsePostersInner.from_dict(movie_images200_response_posters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



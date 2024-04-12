# MovieImages200ResponseBackdropsInner


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
from openapi_client.models.movie_images200_response_backdrops_inner import MovieImages200ResponseBackdropsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieImages200ResponseBackdropsInner from a JSON string
movie_images200_response_backdrops_inner_instance = MovieImages200ResponseBackdropsInner.from_json(json)
# print the JSON string representation of the object
print(MovieImages200ResponseBackdropsInner.to_json())

# convert the object into a dict
movie_images200_response_backdrops_inner_dict = movie_images200_response_backdrops_inner_instance.to_dict()
# create an instance of MovieImages200ResponseBackdropsInner from a dict
movie_images200_response_backdrops_inner_from_dict = MovieImages200ResponseBackdropsInner.from_dict(movie_images200_response_backdrops_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MovieDetails200ResponseGenresInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**name** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.movie_details200_response_genres_inner import MovieDetails200ResponseGenresInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieDetails200ResponseGenresInner from a JSON string
movie_details200_response_genres_inner_instance = MovieDetails200ResponseGenresInner.from_json(json)
# print the JSON string representation of the object
print(MovieDetails200ResponseGenresInner.to_json())

# convert the object into a dict
movie_details200_response_genres_inner_dict = movie_details200_response_genres_inner_instance.to_dict()
# create an instance of MovieDetails200ResponseGenresInner from a dict
movie_details200_response_genres_inner_from_dict = MovieDetails200ResponseGenresInner.from_dict(movie_details200_response_genres_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



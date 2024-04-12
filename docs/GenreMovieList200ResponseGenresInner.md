# GenreMovieList200ResponseGenresInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**name** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.genre_movie_list200_response_genres_inner import GenreMovieList200ResponseGenresInner

# TODO update the JSON string below
json = "{}"
# create an instance of GenreMovieList200ResponseGenresInner from a JSON string
genre_movie_list200_response_genres_inner_instance = GenreMovieList200ResponseGenresInner.from_json(json)
# print the JSON string representation of the object
print(GenreMovieList200ResponseGenresInner.to_json())

# convert the object into a dict
genre_movie_list200_response_genres_inner_dict = genre_movie_list200_response_genres_inner_instance.to_dict()
# create an instance of GenreMovieList200ResponseGenresInner from a dict
genre_movie_list200_response_genres_inner_from_dict = GenreMovieList200ResponseGenresInner.from_dict(genre_movie_list200_response_genres_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GenreMovieList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genres** | [**List[GenreMovieList200ResponseGenresInner]**](GenreMovieList200ResponseGenresInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.genre_movie_list200_response import GenreMovieList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GenreMovieList200Response from a JSON string
genre_movie_list200_response_instance = GenreMovieList200Response.from_json(json)
# print the JSON string representation of the object
print(GenreMovieList200Response.to_json())

# convert the object into a dict
genre_movie_list200_response_dict = genre_movie_list200_response_instance.to_dict()
# create an instance of GenreMovieList200Response from a dict
genre_movie_list200_response_from_dict = GenreMovieList200Response.from_dict(genre_movie_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MovieAddRating200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | [optional] [default to 0]
**status_message** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.movie_add_rating200_response import MovieAddRating200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieAddRating200Response from a JSON string
movie_add_rating200_response_instance = MovieAddRating200Response.from_json(json)
# print the JSON string representation of the object
print(MovieAddRating200Response.to_json())

# convert the object into a dict
movie_add_rating200_response_dict = movie_add_rating200_response_instance.to_dict()
# create an instance of MovieAddRating200Response from a dict
movie_add_rating200_response_from_dict = MovieAddRating200Response.from_dict(movie_add_rating200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



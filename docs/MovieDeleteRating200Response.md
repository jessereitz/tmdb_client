# MovieDeleteRating200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | [optional] [default to 0]
**status_message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.movie_delete_rating200_response import MovieDeleteRating200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieDeleteRating200Response from a JSON string
movie_delete_rating200_response_instance = MovieDeleteRating200Response.from_json(json)
# print the JSON string representation of the object
print(MovieDeleteRating200Response.to_json())

# convert the object into a dict
movie_delete_rating200_response_dict = movie_delete_rating200_response_instance.to_dict()
# create an instance of MovieDeleteRating200Response from a dict
movie_delete_rating200_response_from_dict = MovieDeleteRating200Response.from_dict(movie_delete_rating200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



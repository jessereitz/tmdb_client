# MovieAddRatingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_body** | **str** |  | 

## Example

```python
from openapi_client.models.movie_add_rating_request import MovieAddRatingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MovieAddRatingRequest from a JSON string
movie_add_rating_request_instance = MovieAddRatingRequest.from_json(json)
# print the JSON string representation of the object
print(MovieAddRatingRequest.to_json())

# convert the object into a dict
movie_add_rating_request_dict = movie_add_rating_request_instance.to_dict()
# create an instance of MovieAddRatingRequest from a dict
movie_add_rating_request_from_dict = MovieAddRatingRequest.from_dict(movie_add_rating_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



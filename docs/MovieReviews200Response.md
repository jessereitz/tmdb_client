# MovieReviews200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[MovieReviews200ResponseResultsInner]**](MovieReviews200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.movie_reviews200_response import MovieReviews200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieReviews200Response from a JSON string
movie_reviews200_response_instance = MovieReviews200Response.from_json(json)
# print the JSON string representation of the object
print(MovieReviews200Response.to_json())

# convert the object into a dict
movie_reviews200_response_dict = movie_reviews200_response_instance.to_dict()
# create an instance of MovieReviews200Response from a dict
movie_reviews200_response_from_dict = MovieReviews200Response.from_dict(movie_reviews200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



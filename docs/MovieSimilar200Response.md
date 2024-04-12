# MovieSimilar200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[MovieSimilar200ResponseResultsInner]**](MovieSimilar200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.movie_similar200_response import MovieSimilar200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieSimilar200Response from a JSON string
movie_similar200_response_instance = MovieSimilar200Response.from_json(json)
# print the JSON string representation of the object
print(MovieSimilar200Response.to_json())

# convert the object into a dict
movie_similar200_response_dict = movie_similar200_response_instance.to_dict()
# create an instance of MovieSimilar200Response from a dict
movie_similar200_response_from_dict = MovieSimilar200Response.from_dict(movie_similar200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MoviePopularList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[MoviePopularList200ResponseResultsInner]**](MoviePopularList200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.movie_popular_list200_response import MoviePopularList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MoviePopularList200Response from a JSON string
movie_popular_list200_response_instance = MoviePopularList200Response.from_json(json)
# print the JSON string representation of the object
print(MoviePopularList200Response.to_json())

# convert the object into a dict
movie_popular_list200_response_dict = movie_popular_list200_response_instance.to_dict()
# create an instance of MoviePopularList200Response from a dict
movie_popular_list200_response_from_dict = MoviePopularList200Response.from_dict(movie_popular_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



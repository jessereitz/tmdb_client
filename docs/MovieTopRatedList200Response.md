# MovieTopRatedList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[MovieTopRatedList200ResponseResultsInner]**](MovieTopRatedList200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.movie_top_rated_list200_response import MovieTopRatedList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieTopRatedList200Response from a JSON string
movie_top_rated_list200_response_instance = MovieTopRatedList200Response.from_json(json)
# print the JSON string representation of the object
print(MovieTopRatedList200Response.to_json())

# convert the object into a dict
movie_top_rated_list200_response_dict = movie_top_rated_list200_response_instance.to_dict()
# create an instance of MovieTopRatedList200Response from a dict
movie_top_rated_list200_response_from_dict = MovieTopRatedList200Response.from_dict(movie_top_rated_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



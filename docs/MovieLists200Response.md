# MovieLists200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[MovieLists200ResponseResultsInner]**](MovieLists200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.movie_lists200_response import MovieLists200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieLists200Response from a JSON string
movie_lists200_response_instance = MovieLists200Response.from_json(json)
# print the JSON string representation of the object
print(MovieLists200Response.to_json())

# convert the object into a dict
movie_lists200_response_dict = movie_lists200_response_instance.to_dict()
# create an instance of MovieLists200Response from a dict
movie_lists200_response_from_dict = MovieLists200Response.from_dict(movie_lists200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



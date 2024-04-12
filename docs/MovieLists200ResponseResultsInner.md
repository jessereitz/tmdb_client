# MovieLists200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**favorite_count** | **int** |  | [optional] [default to 0]
**id** | **int** |  | [optional] [default to 0]
**item_count** | **int** |  | [optional] [default to 0]
**iso_639_1** | **str** |  | [optional] 
**list_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**poster_path** | **object** |  | [optional] 

## Example

```python
from tmdb_client.models.movie_lists200_response_results_inner import MovieLists200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieLists200ResponseResultsInner from a JSON string
movie_lists200_response_results_inner_instance = MovieLists200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(MovieLists200ResponseResultsInner.to_json())

# convert the object into a dict
movie_lists200_response_results_inner_dict = movie_lists200_response_results_inner_instance.to_dict()
# create an instance of MovieLists200ResponseResultsInner from a dict
movie_lists200_response_results_inner_from_dict = MovieLists200ResponseResultsInner.from_dict(movie_lists200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



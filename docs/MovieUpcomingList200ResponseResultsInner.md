# MovieUpcomingList200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**backdrop_path** | **str** |  | [optional] 
**genre_ids** | **List[int]** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**original_language** | **str** |  | [optional] 
**original_title** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**poster_path** | **str** |  | [optional] 
**release_date** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**video** | **bool** |  | [optional] [default to True]
**vote_average** | **int** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.movie_upcoming_list200_response_results_inner import MovieUpcomingList200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieUpcomingList200ResponseResultsInner from a JSON string
movie_upcoming_list200_response_results_inner_instance = MovieUpcomingList200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(MovieUpcomingList200ResponseResultsInner.to_json())

# convert the object into a dict
movie_upcoming_list200_response_results_inner_dict = movie_upcoming_list200_response_results_inner_instance.to_dict()
# create an instance of MovieUpcomingList200ResponseResultsInner from a dict
movie_upcoming_list200_response_results_inner_from_dict = MovieUpcomingList200ResponseResultsInner.from_dict(movie_upcoming_list200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


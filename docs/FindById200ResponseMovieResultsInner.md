# FindById200ResponseMovieResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**backdrop_path** | **str** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**title** | **str** |  | [optional] 
**original_language** | **str** |  | [optional] 
**original_title** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**poster_path** | **str** |  | [optional] 
**media_type** | **str** |  | [optional] 
**genre_ids** | **List[int]** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**release_date** | **str** |  | [optional] 
**video** | **bool** |  | [optional] [default to True]
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.find_by_id200_response_movie_results_inner import FindById200ResponseMovieResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FindById200ResponseMovieResultsInner from a JSON string
find_by_id200_response_movie_results_inner_instance = FindById200ResponseMovieResultsInner.from_json(json)
# print the JSON string representation of the object
print(FindById200ResponseMovieResultsInner.to_json())

# convert the object into a dict
find_by_id200_response_movie_results_inner_dict = find_by_id200_response_movie_results_inner_instance.to_dict()
# create an instance of FindById200ResponseMovieResultsInner from a dict
find_by_id200_response_movie_results_inner_from_dict = FindById200ResponseMovieResultsInner.from_dict(find_by_id200_response_movie_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



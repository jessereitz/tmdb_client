# SearchMovie200ResponseResultsInner


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
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.search_movie200_response_results_inner import SearchMovie200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchMovie200ResponseResultsInner from a JSON string
search_movie200_response_results_inner_instance = SearchMovie200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(SearchMovie200ResponseResultsInner.to_json())

# convert the object into a dict
search_movie200_response_results_inner_dict = search_movie200_response_results_inner_instance.to_dict()
# create an instance of SearchMovie200ResponseResultsInner from a dict
search_movie200_response_results_inner_from_dict = SearchMovie200ResponseResultsInner.from_dict(search_movie200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


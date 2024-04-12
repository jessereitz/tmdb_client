# SearchCollection200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**backdrop_path** | **str** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**name** | **str** |  | [optional] 
**original_language** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**poster_path** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.search_collection200_response_results_inner import SearchCollection200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchCollection200ResponseResultsInner from a JSON string
search_collection200_response_results_inner_instance = SearchCollection200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(SearchCollection200ResponseResultsInner.to_json())

# convert the object into a dict
search_collection200_response_results_inner_dict = search_collection200_response_results_inner_instance.to_dict()
# create an instance of SearchCollection200ResponseResultsInner from a dict
search_collection200_response_results_inner_from_dict = SearchCollection200ResponseResultsInner.from_dict(search_collection200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ListsCopy200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**favorite_count** | **int** |  | [optional] [default to 0]
**id** | **int** |  | [optional] [default to 0]
**item_count** | **int** |  | [optional] [default to 0]
**iso_639_1** | **str** |  | [optional] 
**iso_3166_1** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**poster_path** | **object** |  | [optional] 

## Example

```python
from tmdb_client.models.lists_copy200_response_results_inner import ListsCopy200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListsCopy200ResponseResultsInner from a JSON string
lists_copy200_response_results_inner_instance = ListsCopy200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(ListsCopy200ResponseResultsInner.to_json())

# convert the object into a dict
lists_copy200_response_results_inner_dict = lists_copy200_response_results_inner_instance.to_dict()
# create an instance of ListsCopy200ResponseResultsInner from a dict
lists_copy200_response_results_inner_from_dict = ListsCopy200ResponseResultsInner.from_dict(lists_copy200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



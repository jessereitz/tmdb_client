# ListDetails200ResponseItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**backdrop_path** | **str** |  | [optional] 
**genre_ids** | **List[int]** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**media_type** | **str** |  | [optional] 
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
from tmdb_client.models.list_details200_response_items_inner import ListDetails200ResponseItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListDetails200ResponseItemsInner from a JSON string
list_details200_response_items_inner_instance = ListDetails200ResponseItemsInner.from_json(json)
# print the JSON string representation of the object
print(ListDetails200ResponseItemsInner.to_json())

# convert the object into a dict
list_details200_response_items_inner_dict = list_details200_response_items_inner_instance.to_dict()
# create an instance of ListDetails200ResponseItemsInner from a dict
list_details200_response_items_inner_from_dict = ListDetails200ResponseItemsInner.from_dict(list_details200_response_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



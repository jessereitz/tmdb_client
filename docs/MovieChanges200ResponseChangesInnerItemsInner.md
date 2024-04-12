# MovieChanges200ResponseChangesInnerItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**time** | **str** |  | [optional] 
**iso_639_1** | **str** |  | [optional] 
**iso_3166_1** | **str** |  | [optional] 
**value** | [**MovieChanges200ResponseChangesInnerItemsInnerValue**](MovieChanges200ResponseChangesInnerItemsInnerValue.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_changes200_response_changes_inner_items_inner import MovieChanges200ResponseChangesInnerItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieChanges200ResponseChangesInnerItemsInner from a JSON string
movie_changes200_response_changes_inner_items_inner_instance = MovieChanges200ResponseChangesInnerItemsInner.from_json(json)
# print the JSON string representation of the object
print(MovieChanges200ResponseChangesInnerItemsInner.to_json())

# convert the object into a dict
movie_changes200_response_changes_inner_items_inner_dict = movie_changes200_response_changes_inner_items_inner_instance.to_dict()
# create an instance of MovieChanges200ResponseChangesInnerItemsInner from a dict
movie_changes200_response_changes_inner_items_inner_from_dict = MovieChanges200ResponseChangesInnerItemsInner.from_dict(movie_changes200_response_changes_inner_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



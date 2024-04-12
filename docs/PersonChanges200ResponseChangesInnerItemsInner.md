# PersonChanges200ResponseChangesInnerItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**time** | **str** |  | [optional] 
**iso_639_1** | **str** |  | [optional] 
**iso_3166_1** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.person_changes200_response_changes_inner_items_inner import PersonChanges200ResponseChangesInnerItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PersonChanges200ResponseChangesInnerItemsInner from a JSON string
person_changes200_response_changes_inner_items_inner_instance = PersonChanges200ResponseChangesInnerItemsInner.from_json(json)
# print the JSON string representation of the object
print(PersonChanges200ResponseChangesInnerItemsInner.to_json())

# convert the object into a dict
person_changes200_response_changes_inner_items_inner_dict = person_changes200_response_changes_inner_items_inner_instance.to_dict()
# create an instance of PersonChanges200ResponseChangesInnerItemsInner from a dict
person_changes200_response_changes_inner_items_inner_from_dict = PersonChanges200ResponseChangesInnerItemsInner.from_dict(person_changes200_response_changes_inner_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



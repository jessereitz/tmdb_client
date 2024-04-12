# PersonChanges200ResponseChangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**items** | [**List[PersonChanges200ResponseChangesInnerItemsInner]**](PersonChanges200ResponseChangesInnerItemsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.person_changes200_response_changes_inner import PersonChanges200ResponseChangesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PersonChanges200ResponseChangesInner from a JSON string
person_changes200_response_changes_inner_instance = PersonChanges200ResponseChangesInner.from_json(json)
# print the JSON string representation of the object
print(PersonChanges200ResponseChangesInner.to_json())

# convert the object into a dict
person_changes200_response_changes_inner_dict = person_changes200_response_changes_inner_instance.to_dict()
# create an instance of PersonChanges200ResponseChangesInner from a dict
person_changes200_response_changes_inner_from_dict = PersonChanges200ResponseChangesInner.from_dict(person_changes200_response_changes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PersonChanges200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**List[PersonChanges200ResponseChangesInner]**](PersonChanges200ResponseChangesInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.person_changes200_response import PersonChanges200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PersonChanges200Response from a JSON string
person_changes200_response_instance = PersonChanges200Response.from_json(json)
# print the JSON string representation of the object
print(PersonChanges200Response.to_json())

# convert the object into a dict
person_changes200_response_dict = person_changes200_response_instance.to_dict()
# create an instance of PersonChanges200Response from a dict
person_changes200_response_from_dict = PersonChanges200Response.from_dict(person_changes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PersonImages200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**profiles** | [**List[PersonImages200ResponseProfilesInner]**](PersonImages200ResponseProfilesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.person_images200_response import PersonImages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PersonImages200Response from a JSON string
person_images200_response_instance = PersonImages200Response.from_json(json)
# print the JSON string representation of the object
print(PersonImages200Response.to_json())

# convert the object into a dict
person_images200_response_dict = person_images200_response_instance.to_dict()
# create an instance of PersonImages200Response from a dict
person_images200_response_from_dict = PersonImages200Response.from_dict(person_images200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



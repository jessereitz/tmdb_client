# ListCreate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] [default to True]
**status_code** | **int** |  | [optional] [default to 0]
**list_id** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.list_create200_response import ListCreate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListCreate200Response from a JSON string
list_create200_response_instance = ListCreate200Response.from_json(json)
# print the JSON string representation of the object
print(ListCreate200Response.to_json())

# convert the object into a dict
list_create200_response_dict = list_create200_response_instance.to_dict()
# create an instance of ListCreate200Response from a dict
list_create200_response_from_dict = ListCreate200Response.from_dict(list_create200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



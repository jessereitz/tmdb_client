# ListDelete200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | [optional] [default to 0]
**status_message** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.list_delete200_response import ListDelete200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDelete200Response from a JSON string
list_delete200_response_instance = ListDelete200Response.from_json(json)
# print the JSON string representation of the object
print(ListDelete200Response.to_json())

# convert the object into a dict
list_delete200_response_dict = list_delete200_response_instance.to_dict()
# create an instance of ListDelete200Response from a dict
list_delete200_response_from_dict = ListDelete200Response.from_dict(list_delete200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



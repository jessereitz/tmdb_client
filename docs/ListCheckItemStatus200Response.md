# ListCheckItemStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**item_present** | **bool** |  | [optional] [default to True]

## Example

```python
from tmdb_client.models.list_check_item_status200_response import ListCheckItemStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListCheckItemStatus200Response from a JSON string
list_check_item_status200_response_instance = ListCheckItemStatus200Response.from_json(json)
# print the JSON string representation of the object
print(ListCheckItemStatus200Response.to_json())

# convert the object into a dict
list_check_item_status200_response_dict = list_check_item_status200_response_instance.to_dict()
# create an instance of ListCheckItemStatus200Response from a dict
list_check_item_status200_response_from_dict = ListCheckItemStatus200Response.from_dict(list_check_item_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



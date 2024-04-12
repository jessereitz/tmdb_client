# ListsCopy200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[ListsCopy200ResponseResultsInner]**](ListsCopy200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.lists_copy200_response import ListsCopy200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListsCopy200Response from a JSON string
lists_copy200_response_instance = ListsCopy200Response.from_json(json)
# print the JSON string representation of the object
print(ListsCopy200Response.to_json())

# convert the object into a dict
lists_copy200_response_dict = lists_copy200_response_instance.to_dict()
# create an instance of ListsCopy200Response from a dict
lists_copy200_response_from_dict = ListsCopy200Response.from_dict(lists_copy200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



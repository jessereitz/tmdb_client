# ListDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**favorite_count** | **int** |  | [optional] [default to 0]
**id** | **str** |  | [optional] 
**items** | [**List[ListDetails200ResponseItemsInner]**](ListDetails200ResponseItemsInner.md) |  | [optional] 
**item_count** | **int** |  | [optional] [default to 0]
**iso_639_1** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**poster_path** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.list_details200_response import ListDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDetails200Response from a JSON string
list_details200_response_instance = ListDetails200Response.from_json(json)
# print the JSON string representation of the object
print(ListDetails200Response.to_json())

# convert the object into a dict
list_details200_response_dict = list_details200_response_instance.to_dict()
# create an instance of ListDetails200Response from a dict
list_details200_response_from_dict = ListDetails200Response.from_dict(list_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



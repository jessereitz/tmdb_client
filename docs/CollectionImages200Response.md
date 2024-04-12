# CollectionImages200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**backdrops** | [**List[CollectionImages200ResponseBackdropsInner]**](CollectionImages200ResponseBackdropsInner.md) |  | [optional] 
**posters** | [**List[CollectionImages200ResponsePostersInner]**](CollectionImages200ResponsePostersInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.collection_images200_response import CollectionImages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionImages200Response from a JSON string
collection_images200_response_instance = CollectionImages200Response.from_json(json)
# print the JSON string representation of the object
print(CollectionImages200Response.to_json())

# convert the object into a dict
collection_images200_response_dict = collection_images200_response_instance.to_dict()
# create an instance of CollectionImages200Response from a dict
collection_images200_response_from_dict = CollectionImages200Response.from_dict(collection_images200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



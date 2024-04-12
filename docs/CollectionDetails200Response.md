# CollectionDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**poster_path** | **str** |  | [optional] 
**backdrop_path** | **str** |  | [optional] 
**parts** | [**List[CollectionDetails200ResponsePartsInner]**](CollectionDetails200ResponsePartsInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.collection_details200_response import CollectionDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionDetails200Response from a JSON string
collection_details200_response_instance = CollectionDetails200Response.from_json(json)
# print the JSON string representation of the object
print(CollectionDetails200Response.to_json())

# convert the object into a dict
collection_details200_response_dict = collection_details200_response_instance.to_dict()
# create an instance of CollectionDetails200Response from a dict
collection_details200_response_from_dict = CollectionDetails200Response.from_dict(collection_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



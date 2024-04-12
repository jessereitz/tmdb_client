# CollectionDetails200ResponsePartsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**backdrop_path** | **str** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**title** | **str** |  | [optional] 
**original_language** | **str** |  | [optional] 
**original_title** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**poster_path** | **str** |  | [optional] 
**media_type** | **str** |  | [optional] 
**genre_ids** | **List[int]** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**release_date** | **str** |  | [optional] 
**video** | **bool** |  | [optional] [default to True]
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.collection_details200_response_parts_inner import CollectionDetails200ResponsePartsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionDetails200ResponsePartsInner from a JSON string
collection_details200_response_parts_inner_instance = CollectionDetails200ResponsePartsInner.from_json(json)
# print the JSON string representation of the object
print(CollectionDetails200ResponsePartsInner.to_json())

# convert the object into a dict
collection_details200_response_parts_inner_dict = collection_details200_response_parts_inner_instance.to_dict()
# create an instance of CollectionDetails200ResponsePartsInner from a dict
collection_details200_response_parts_inner_from_dict = CollectionDetails200ResponsePartsInner.from_dict(collection_details200_response_parts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


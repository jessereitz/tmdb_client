# PersonTaggedImages200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_ratio** | **float** |  | [optional] [default to 0]
**file_path** | **str** |  | [optional] 
**height** | **int** |  | [optional] [default to 0]
**id** | **str** |  | [optional] 
**iso_639_1** | **str** |  | [optional] 
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]
**width** | **int** |  | [optional] [default to 0]
**image_type** | **str** |  | [optional] 
**media** | [**PersonTaggedImages200ResponseResultsInnerMedia**](PersonTaggedImages200ResponseResultsInnerMedia.md) |  | [optional] 
**media_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.person_tagged_images200_response_results_inner import PersonTaggedImages200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PersonTaggedImages200ResponseResultsInner from a JSON string
person_tagged_images200_response_results_inner_instance = PersonTaggedImages200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(PersonTaggedImages200ResponseResultsInner.to_json())

# convert the object into a dict
person_tagged_images200_response_results_inner_dict = person_tagged_images200_response_results_inner_instance.to_dict()
# create an instance of PersonTaggedImages200ResponseResultsInner from a dict
person_tagged_images200_response_results_inner_from_dict = PersonTaggedImages200ResponseResultsInner.from_dict(person_tagged_images200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



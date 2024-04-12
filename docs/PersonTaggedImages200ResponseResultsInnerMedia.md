# PersonTaggedImages200ResponseResultsInnerMedia


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
from tmdb_client.models.person_tagged_images200_response_results_inner_media import PersonTaggedImages200ResponseResultsInnerMedia

# TODO update the JSON string below
json = "{}"
# create an instance of PersonTaggedImages200ResponseResultsInnerMedia from a JSON string
person_tagged_images200_response_results_inner_media_instance = PersonTaggedImages200ResponseResultsInnerMedia.from_json(json)
# print the JSON string representation of the object
print(PersonTaggedImages200ResponseResultsInnerMedia.to_json())

# convert the object into a dict
person_tagged_images200_response_results_inner_media_dict = person_tagged_images200_response_results_inner_media_instance.to_dict()
# create an instance of PersonTaggedImages200ResponseResultsInnerMedia from a dict
person_tagged_images200_response_results_inner_media_from_dict = PersonTaggedImages200ResponseResultsInnerMedia.from_dict(person_tagged_images200_response_results_inner_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PersonImages200ResponseProfilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_ratio** | **float** |  | [optional] [default to 0]
**height** | **int** |  | [optional] [default to 0]
**iso_639_1** | **object** |  | [optional] 
**file_path** | **str** |  | [optional] 
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]
**width** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.person_images200_response_profiles_inner import PersonImages200ResponseProfilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PersonImages200ResponseProfilesInner from a JSON string
person_images200_response_profiles_inner_instance = PersonImages200ResponseProfilesInner.from_json(json)
# print the JSON string representation of the object
print(PersonImages200ResponseProfilesInner.to_json())

# convert the object into a dict
person_images200_response_profiles_inner_dict = person_images200_response_profiles_inner_instance.to_dict()
# create an instance of PersonImages200ResponseProfilesInner from a dict
person_images200_response_profiles_inner_from_dict = PersonImages200ResponseProfilesInner.from_dict(person_images200_response_profiles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



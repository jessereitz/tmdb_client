# PersonLatestId200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**also_known_as** | **List[str]** |  | [optional] 
**biography** | **str** |  | [optional] 
**birthday** | **object** |  | [optional] 
**deathday** | **object** |  | [optional] 
**gender** | **int** |  | [optional] [default to 0]
**homepage** | **object** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**imdb_id** | **object** |  | [optional] 
**known_for_department** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**place_of_birth** | **object** |  | [optional] 
**popularity** | **int** |  | [optional] [default to 0]
**profile_path** | **object** |  | [optional] 

## Example

```python
from tmdb_client.models.person_latest_id200_response import PersonLatestId200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PersonLatestId200Response from a JSON string
person_latest_id200_response_instance = PersonLatestId200Response.from_json(json)
# print the JSON string representation of the object
print(PersonLatestId200Response.to_json())

# convert the object into a dict
person_latest_id200_response_dict = person_latest_id200_response_instance.to_dict()
# create an instance of PersonLatestId200Response from a dict
person_latest_id200_response_from_dict = PersonLatestId200Response.from_dict(person_latest_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



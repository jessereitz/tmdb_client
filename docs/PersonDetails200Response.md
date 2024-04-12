# PersonDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**also_known_as** | **List[str]** |  | [optional] 
**biography** | **str** |  | [optional] 
**birthday** | **str** |  | [optional] 
**deathday** | **object** |  | [optional] 
**gender** | **int** |  | [optional] [default to 0]
**homepage** | **object** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**imdb_id** | **str** |  | [optional] 
**known_for_department** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**place_of_birth** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**profile_path** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.person_details200_response import PersonDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PersonDetails200Response from a JSON string
person_details200_response_instance = PersonDetails200Response.from_json(json)
# print the JSON string representation of the object
print(PersonDetails200Response.to_json())

# convert the object into a dict
person_details200_response_dict = person_details200_response_instance.to_dict()
# create an instance of PersonDetails200Response from a dict
person_details200_response_from_dict = PersonDetails200Response.from_dict(person_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



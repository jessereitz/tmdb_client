# PersonCombinedCredits200ResponseCrewInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**backdrop_path** | **str** |  | [optional] 
**genre_ids** | **List[int]** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**original_language** | **str** |  | [optional] 
**original_title** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**poster_path** | **str** |  | [optional] 
**release_date** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**video** | **bool** |  | [optional] [default to True]
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]
**credit_id** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**job** | **str** |  | [optional] 
**media_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.person_combined_credits200_response_crew_inner import PersonCombinedCredits200ResponseCrewInner

# TODO update the JSON string below
json = "{}"
# create an instance of PersonCombinedCredits200ResponseCrewInner from a JSON string
person_combined_credits200_response_crew_inner_instance = PersonCombinedCredits200ResponseCrewInner.from_json(json)
# print the JSON string representation of the object
print(PersonCombinedCredits200ResponseCrewInner.to_json())

# convert the object into a dict
person_combined_credits200_response_crew_inner_dict = person_combined_credits200_response_crew_inner_instance.to_dict()
# create an instance of PersonCombinedCredits200ResponseCrewInner from a dict
person_combined_credits200_response_crew_inner_from_dict = PersonCombinedCredits200ResponseCrewInner.from_dict(person_combined_credits200_response_crew_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



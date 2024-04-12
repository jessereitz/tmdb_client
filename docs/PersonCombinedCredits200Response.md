# PersonCombinedCredits200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cast** | [**List[PersonCombinedCredits200ResponseCastInner]**](PersonCombinedCredits200ResponseCastInner.md) |  | [optional] 
**crew** | [**List[PersonCombinedCredits200ResponseCrewInner]**](PersonCombinedCredits200ResponseCrewInner.md) |  | [optional] 
**id** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.person_combined_credits200_response import PersonCombinedCredits200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PersonCombinedCredits200Response from a JSON string
person_combined_credits200_response_instance = PersonCombinedCredits200Response.from_json(json)
# print the JSON string representation of the object
print(PersonCombinedCredits200Response.to_json())

# convert the object into a dict
person_combined_credits200_response_dict = person_combined_credits200_response_instance.to_dict()
# create an instance of PersonCombinedCredits200Response from a dict
person_combined_credits200_response_from_dict = PersonCombinedCredits200Response.from_dict(person_combined_credits200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



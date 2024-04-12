# PersonTvCredits200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cast** | [**List[PersonTvCredits200ResponseCastInner]**](PersonTvCredits200ResponseCastInner.md) |  | [optional] 
**crew** | [**List[PersonTvCredits200ResponseCrewInner]**](PersonTvCredits200ResponseCrewInner.md) |  | [optional] 
**id** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.person_tv_credits200_response import PersonTvCredits200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PersonTvCredits200Response from a JSON string
person_tv_credits200_response_instance = PersonTvCredits200Response.from_json(json)
# print the JSON string representation of the object
print(PersonTvCredits200Response.to_json())

# convert the object into a dict
person_tv_credits200_response_dict = person_tv_credits200_response_instance.to_dict()
# create an instance of PersonTvCredits200Response from a dict
person_tv_credits200_response_from_dict = PersonTvCredits200Response.from_dict(person_tv_credits200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



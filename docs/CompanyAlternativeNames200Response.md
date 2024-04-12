# CompanyAlternativeNames200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**results** | [**List[CompanyAlternativeNames200ResponseResultsInner]**](CompanyAlternativeNames200ResponseResultsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.company_alternative_names200_response import CompanyAlternativeNames200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyAlternativeNames200Response from a JSON string
company_alternative_names200_response_instance = CompanyAlternativeNames200Response.from_json(json)
# print the JSON string representation of the object
print(CompanyAlternativeNames200Response.to_json())

# convert the object into a dict
company_alternative_names200_response_dict = company_alternative_names200_response_instance.to_dict()
# create an instance of CompanyAlternativeNames200Response from a dict
company_alternative_names200_response_from_dict = CompanyAlternativeNames200Response.from_dict(company_alternative_names200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



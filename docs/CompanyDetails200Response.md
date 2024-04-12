# CompanyDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**headquarters** | **str** |  | [optional] 
**homepage** | **str** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**logo_path** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**origin_country** | **str** |  | [optional] 
**parent_company** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.company_details200_response import CompanyDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyDetails200Response from a JSON string
company_details200_response_instance = CompanyDetails200Response.from_json(json)
# print the JSON string representation of the object
print(CompanyDetails200Response.to_json())

# convert the object into a dict
company_details200_response_dict = company_details200_response_instance.to_dict()
# create an instance of CompanyDetails200Response from a dict
company_details200_response_from_dict = CompanyDetails200Response.from_dict(company_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



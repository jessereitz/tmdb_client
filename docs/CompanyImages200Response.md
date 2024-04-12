# CompanyImages200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**logos** | [**List[CompanyImages200ResponseLogosInner]**](CompanyImages200ResponseLogosInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.company_images200_response import CompanyImages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyImages200Response from a JSON string
company_images200_response_instance = CompanyImages200Response.from_json(json)
# print the JSON string representation of the object
print(CompanyImages200Response.to_json())

# convert the object into a dict
company_images200_response_dict = company_images200_response_instance.to_dict()
# create an instance of CompanyImages200Response from a dict
company_images200_response_from_dict = CompanyImages200Response.from_dict(company_images200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



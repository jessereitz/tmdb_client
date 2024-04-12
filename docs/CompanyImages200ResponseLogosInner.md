# CompanyImages200ResponseLogosInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_ratio** | **float** |  | [optional] [default to 0]
**file_path** | **str** |  | [optional] 
**height** | **int** |  | [optional] [default to 0]
**id** | **str** |  | [optional] 
**file_type** | **str** |  | [optional] 
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]
**width** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.company_images200_response_logos_inner import CompanyImages200ResponseLogosInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyImages200ResponseLogosInner from a JSON string
company_images200_response_logos_inner_instance = CompanyImages200ResponseLogosInner.from_json(json)
# print the JSON string representation of the object
print(CompanyImages200ResponseLogosInner.to_json())

# convert the object into a dict
company_images200_response_logos_inner_dict = company_images200_response_logos_inner_instance.to_dict()
# create an instance of CompanyImages200ResponseLogosInner from a dict
company_images200_response_logos_inner_from_dict = CompanyImages200ResponseLogosInner.from_dict(company_images200_response_logos_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



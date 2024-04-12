# SearchCompany200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**logo_path** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**origin_country** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.search_company200_response_results_inner import SearchCompany200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchCompany200ResponseResultsInner from a JSON string
search_company200_response_results_inner_instance = SearchCompany200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(SearchCompany200ResponseResultsInner.to_json())

# convert the object into a dict
search_company200_response_results_inner_dict = search_company200_response_results_inner_instance.to_dict()
# create an instance of SearchCompany200ResponseResultsInner from a dict
search_company200_response_results_inner_from_dict = SearchCompany200ResponseResultsInner.from_dict(search_company200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SearchTv200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[SearchTv200ResponseResultsInner]**](SearchTv200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.search_tv200_response import SearchTv200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTv200Response from a JSON string
search_tv200_response_instance = SearchTv200Response.from_json(json)
# print the JSON string representation of the object
print(SearchTv200Response.to_json())

# convert the object into a dict
search_tv200_response_dict = search_tv200_response_instance.to_dict()
# create an instance of SearchTv200Response from a dict
search_tv200_response_from_dict = SearchTv200Response.from_dict(search_tv200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



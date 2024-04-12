# DiscoverTv200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[DiscoverTv200ResponseResultsInner]**](DiscoverTv200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.discover_tv200_response import DiscoverTv200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoverTv200Response from a JSON string
discover_tv200_response_instance = DiscoverTv200Response.from_json(json)
# print the JSON string representation of the object
print(DiscoverTv200Response.to_json())

# convert the object into a dict
discover_tv200_response_dict = discover_tv200_response_instance.to_dict()
# create an instance of DiscoverTv200Response from a dict
discover_tv200_response_from_dict = DiscoverTv200Response.from_dict(discover_tv200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



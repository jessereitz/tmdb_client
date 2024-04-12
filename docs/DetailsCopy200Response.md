# DetailsCopy200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**results** | [**List[DetailsCopy200ResponseResultsInner]**](DetailsCopy200ResponseResultsInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.details_copy200_response import DetailsCopy200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DetailsCopy200Response from a JSON string
details_copy200_response_instance = DetailsCopy200Response.from_json(json)
# print the JSON string representation of the object
print(DetailsCopy200Response.to_json())

# convert the object into a dict
details_copy200_response_dict = details_copy200_response_instance.to_dict()
# create an instance of DetailsCopy200Response from a dict
details_copy200_response_from_dict = DetailsCopy200Response.from_dict(details_copy200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



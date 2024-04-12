# AlternativeNamesCopy200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**logos** | [**List[AlternativeNamesCopy200ResponseLogosInner]**](AlternativeNamesCopy200ResponseLogosInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.alternative_names_copy200_response import AlternativeNamesCopy200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AlternativeNamesCopy200Response from a JSON string
alternative_names_copy200_response_instance = AlternativeNamesCopy200Response.from_json(json)
# print the JSON string representation of the object
print(AlternativeNamesCopy200Response.to_json())

# convert the object into a dict
alternative_names_copy200_response_dict = alternative_names_copy200_response_instance.to_dict()
# create an instance of AlternativeNamesCopy200Response from a dict
alternative_names_copy200_response_from_dict = AlternativeNamesCopy200Response.from_dict(alternative_names_copy200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



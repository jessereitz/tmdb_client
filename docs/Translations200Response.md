# Translations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**translations** | [**List[Translations200ResponseTranslationsInner]**](Translations200ResponseTranslationsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.translations200_response import Translations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Translations200Response from a JSON string
translations200_response_instance = Translations200Response.from_json(json)
# print the JSON string representation of the object
print(Translations200Response.to_json())

# convert the object into a dict
translations200_response_dict = translations200_response_instance.to_dict()
# create an instance of Translations200Response from a dict
translations200_response_from_dict = Translations200Response.from_dict(translations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



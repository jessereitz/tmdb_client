# AuthenticationValidateKey200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**status_code** | **int** |  | [optional] [default to 0]
**status_message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.authentication_validate_key200_response import AuthenticationValidateKey200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationValidateKey200Response from a JSON string
authentication_validate_key200_response_instance = AuthenticationValidateKey200Response.from_json(json)
# print the JSON string representation of the object
print(AuthenticationValidateKey200Response.to_json())

# convert the object into a dict
authentication_validate_key200_response_dict = authentication_validate_key200_response_instance.to_dict()
# create an instance of AuthenticationValidateKey200Response from a dict
authentication_validate_key200_response_from_dict = AuthenticationValidateKey200Response.from_dict(authentication_validate_key200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



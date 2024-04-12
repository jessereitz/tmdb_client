# AuthenticationValidateKey401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | [optional] [default to 0]
**status_message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] [default to True]

## Example

```python
from tmdb_client.models.authentication_validate_key401_response import AuthenticationValidateKey401Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationValidateKey401Response from a JSON string
authentication_validate_key401_response_instance = AuthenticationValidateKey401Response.from_json(json)
# print the JSON string representation of the object
print(AuthenticationValidateKey401Response.to_json())

# convert the object into a dict
authentication_validate_key401_response_dict = authentication_validate_key401_response_instance.to_dict()
# create an instance of AuthenticationValidateKey401Response from a dict
authentication_validate_key401_response_from_dict = AuthenticationValidateKey401Response.from_dict(authentication_validate_key401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



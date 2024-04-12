# AuthenticationCreateSession200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**session_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.authentication_create_session200_response import AuthenticationCreateSession200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationCreateSession200Response from a JSON string
authentication_create_session200_response_instance = AuthenticationCreateSession200Response.from_json(json)
# print the JSON string representation of the object
print(AuthenticationCreateSession200Response.to_json())

# convert the object into a dict
authentication_create_session200_response_dict = authentication_create_session200_response_instance.to_dict()
# create an instance of AuthenticationCreateSession200Response from a dict
authentication_create_session200_response_from_dict = AuthenticationCreateSession200Response.from_dict(authentication_create_session200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AuthenticationCreateSessionFromV4Token200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**session_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.authentication_create_session_from_v4_token200_response import AuthenticationCreateSessionFromV4Token200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationCreateSessionFromV4Token200Response from a JSON string
authentication_create_session_from_v4_token200_response_instance = AuthenticationCreateSessionFromV4Token200Response.from_json(json)
# print the JSON string representation of the object
print(AuthenticationCreateSessionFromV4Token200Response.to_json())

# convert the object into a dict
authentication_create_session_from_v4_token200_response_dict = authentication_create_session_from_v4_token200_response_instance.to_dict()
# create an instance of AuthenticationCreateSessionFromV4Token200Response from a dict
authentication_create_session_from_v4_token200_response_from_dict = AuthenticationCreateSessionFromV4Token200Response.from_dict(authentication_create_session_from_v4_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AuthenticationDeleteSession200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]

## Example

```python
from tmdb_client.models.authentication_delete_session200_response import AuthenticationDeleteSession200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationDeleteSession200Response from a JSON string
authentication_delete_session200_response_instance = AuthenticationDeleteSession200Response.from_json(json)
# print the JSON string representation of the object
print(AuthenticationDeleteSession200Response.to_json())

# convert the object into a dict
authentication_delete_session200_response_dict = authentication_delete_session200_response_instance.to_dict()
# create an instance of AuthenticationDeleteSession200Response from a dict
authentication_delete_session200_response_from_dict = AuthenticationDeleteSession200Response.from_dict(authentication_delete_session200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



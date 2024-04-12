# AccountDetails200ResponseAvatar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gravatar** | [**AccountDetails200ResponseAvatarGravatar**](AccountDetails200ResponseAvatarGravatar.md) |  | [optional] 
**tmdb** | [**AccountDetails200ResponseAvatarTmdb**](AccountDetails200ResponseAvatarTmdb.md) |  | [optional] 

## Example

```python
from tmdb_client.models.account_details200_response_avatar import AccountDetails200ResponseAvatar

# TODO update the JSON string below
json = "{}"
# create an instance of AccountDetails200ResponseAvatar from a JSON string
account_details200_response_avatar_instance = AccountDetails200ResponseAvatar.from_json(json)
# print the JSON string representation of the object
print(AccountDetails200ResponseAvatar.to_json())

# convert the object into a dict
account_details200_response_avatar_dict = account_details200_response_avatar_instance.to_dict()
# create an instance of AccountDetails200ResponseAvatar from a dict
account_details200_response_avatar_from_dict = AccountDetails200ResponseAvatar.from_dict(account_details200_response_avatar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



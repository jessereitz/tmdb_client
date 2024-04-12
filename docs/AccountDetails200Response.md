# AccountDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar** | [**AccountDetails200ResponseAvatar**](AccountDetails200ResponseAvatar.md) |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**iso_639_1** | **str** |  | [optional] 
**iso_3166_1** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**include_adult** | **bool** |  | [optional] [default to True]
**username** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.account_details200_response import AccountDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AccountDetails200Response from a JSON string
account_details200_response_instance = AccountDetails200Response.from_json(json)
# print the JSON string representation of the object
print(AccountDetails200Response.to_json())

# convert the object into a dict
account_details200_response_dict = account_details200_response_instance.to_dict()
# create an instance of AccountDetails200Response from a dict
account_details200_response_from_dict = AccountDetails200Response.from_dict(account_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



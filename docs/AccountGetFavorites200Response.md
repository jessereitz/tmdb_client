# AccountGetFavorites200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[AccountGetFavorites200ResponseResultsInner]**](AccountGetFavorites200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.account_get_favorites200_response import AccountGetFavorites200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGetFavorites200Response from a JSON string
account_get_favorites200_response_instance = AccountGetFavorites200Response.from_json(json)
# print the JSON string representation of the object
print(AccountGetFavorites200Response.to_json())

# convert the object into a dict
account_get_favorites200_response_dict = account_get_favorites200_response_instance.to_dict()
# create an instance of AccountGetFavorites200Response from a dict
account_get_favorites200_response_from_dict = AccountGetFavorites200Response.from_dict(account_get_favorites200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



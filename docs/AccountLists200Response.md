# AccountLists200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[AccountLists200ResponseResultsInner]**](AccountLists200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.account_lists200_response import AccountLists200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AccountLists200Response from a JSON string
account_lists200_response_instance = AccountLists200Response.from_json(json)
# print the JSON string representation of the object
print(AccountLists200Response.to_json())

# convert the object into a dict
account_lists200_response_dict = account_lists200_response_instance.to_dict()
# create an instance of AccountLists200Response from a dict
account_lists200_response_from_dict = AccountLists200Response.from_dict(account_lists200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



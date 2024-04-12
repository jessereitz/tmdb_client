# AccountRatedTvEpisodes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[AccountRatedTvEpisodes200ResponseResultsInner]**](AccountRatedTvEpisodes200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.account_rated_tv_episodes200_response import AccountRatedTvEpisodes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRatedTvEpisodes200Response from a JSON string
account_rated_tv_episodes200_response_instance = AccountRatedTvEpisodes200Response.from_json(json)
# print the JSON string representation of the object
print(AccountRatedTvEpisodes200Response.to_json())

# convert the object into a dict
account_rated_tv_episodes200_response_dict = account_rated_tv_episodes200_response_instance.to_dict()
# create an instance of AccountRatedTvEpisodes200Response from a dict
account_rated_tv_episodes200_response_from_dict = AccountRatedTvEpisodes200Response.from_dict(account_rated_tv_episodes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GuestSessionRatedTv200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[GuestSessionRatedTv200ResponseResultsInner]**](GuestSessionRatedTv200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.guest_session_rated_tv200_response import GuestSessionRatedTv200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GuestSessionRatedTv200Response from a JSON string
guest_session_rated_tv200_response_instance = GuestSessionRatedTv200Response.from_json(json)
# print the JSON string representation of the object
print(GuestSessionRatedTv200Response.to_json())

# convert the object into a dict
guest_session_rated_tv200_response_dict = guest_session_rated_tv200_response_instance.to_dict()
# create an instance of GuestSessionRatedTv200Response from a dict
guest_session_rated_tv200_response_from_dict = GuestSessionRatedTv200Response.from_dict(guest_session_rated_tv200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



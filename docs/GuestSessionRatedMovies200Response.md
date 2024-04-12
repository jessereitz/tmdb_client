# GuestSessionRatedMovies200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[GuestSessionRatedMovies200ResponseResultsInner]**](GuestSessionRatedMovies200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.guest_session_rated_movies200_response import GuestSessionRatedMovies200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GuestSessionRatedMovies200Response from a JSON string
guest_session_rated_movies200_response_instance = GuestSessionRatedMovies200Response.from_json(json)
# print the JSON string representation of the object
print(GuestSessionRatedMovies200Response.to_json())

# convert the object into a dict
guest_session_rated_movies200_response_dict = guest_session_rated_movies200_response_instance.to_dict()
# create an instance of GuestSessionRatedMovies200Response from a dict
guest_session_rated_movies200_response_from_dict = GuestSessionRatedMovies200Response.from_dict(guest_session_rated_movies200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



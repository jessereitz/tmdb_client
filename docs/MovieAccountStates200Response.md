# MovieAccountStates200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**favorite** | **bool** |  | [optional] [default to True]
**rated** | [**MovieAccountStates200ResponseRated**](MovieAccountStates200ResponseRated.md) |  | [optional] 
**watchlist** | **bool** |  | [optional] [default to True]

## Example

```python
from openapi_client.models.movie_account_states200_response import MovieAccountStates200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieAccountStates200Response from a JSON string
movie_account_states200_response_instance = MovieAccountStates200Response.from_json(json)
# print the JSON string representation of the object
print(MovieAccountStates200Response.to_json())

# convert the object into a dict
movie_account_states200_response_dict = movie_account_states200_response_instance.to_dict()
# create an instance of MovieAccountStates200Response from a dict
movie_account_states200_response_from_dict = MovieAccountStates200Response.from_dict(movie_account_states200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



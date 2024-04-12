# MovieCredits200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**cast** | [**List[MovieCredits200ResponseCastInner]**](MovieCredits200ResponseCastInner.md) |  | [optional] 
**crew** | [**List[MovieCredits200ResponseCrewInner]**](MovieCredits200ResponseCrewInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_credits200_response import MovieCredits200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieCredits200Response from a JSON string
movie_credits200_response_instance = MovieCredits200Response.from_json(json)
# print the JSON string representation of the object
print(MovieCredits200Response.to_json())

# convert the object into a dict
movie_credits200_response_dict = movie_credits200_response_instance.to_dict()
# create an instance of MovieCredits200Response from a dict
movie_credits200_response_from_dict = MovieCredits200Response.from_dict(movie_credits200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



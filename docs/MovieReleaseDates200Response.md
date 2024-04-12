# MovieReleaseDates200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**results** | [**List[MovieReleaseDates200ResponseResultsInner]**](MovieReleaseDates200ResponseResultsInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_release_dates200_response import MovieReleaseDates200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieReleaseDates200Response from a JSON string
movie_release_dates200_response_instance = MovieReleaseDates200Response.from_json(json)
# print the JSON string representation of the object
print(MovieReleaseDates200Response.to_json())

# convert the object into a dict
movie_release_dates200_response_dict = movie_release_dates200_response_instance.to_dict()
# create an instance of MovieReleaseDates200Response from a dict
movie_release_dates200_response_from_dict = MovieReleaseDates200Response.from_dict(movie_release_dates200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



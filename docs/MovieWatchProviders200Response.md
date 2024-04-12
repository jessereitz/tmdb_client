# MovieWatchProviders200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**results** | [**MovieWatchProviders200ResponseResults**](MovieWatchProviders200ResponseResults.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response import MovieWatchProviders200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200Response from a JSON string
movie_watch_providers200_response_instance = MovieWatchProviders200Response.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200Response.to_json())

# convert the object into a dict
movie_watch_providers200_response_dict = movie_watch_providers200_response_instance.to_dict()
# create an instance of MovieWatchProviders200Response from a dict
movie_watch_providers200_response_from_dict = MovieWatchProviders200Response.from_dict(movie_watch_providers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



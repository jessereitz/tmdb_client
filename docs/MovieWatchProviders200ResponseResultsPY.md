# MovieWatchProviders200ResponseResultsPY


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_py import MovieWatchProviders200ResponseResultsPY

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsPY from a JSON string
movie_watch_providers200_response_results_py_instance = MovieWatchProviders200ResponseResultsPY.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsPY.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_py_dict = movie_watch_providers200_response_results_py_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsPY from a dict
movie_watch_providers200_response_results_py_from_dict = MovieWatchProviders200ResponseResultsPY.from_dict(movie_watch_providers200_response_results_py_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



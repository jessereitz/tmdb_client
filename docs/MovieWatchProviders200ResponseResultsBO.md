# MovieWatchProviders200ResponseResultsBO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_bo import MovieWatchProviders200ResponseResultsBO

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsBO from a JSON string
movie_watch_providers200_response_results_bo_instance = MovieWatchProviders200ResponseResultsBO.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsBO.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_bo_dict = movie_watch_providers200_response_results_bo_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsBO from a dict
movie_watch_providers200_response_results_bo_from_dict = MovieWatchProviders200ResponseResultsBO.from_dict(movie_watch_providers200_response_results_bo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



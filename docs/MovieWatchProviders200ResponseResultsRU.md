# MovieWatchProviders200ResponseResultsRU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsRURentInner]**](MovieWatchProviders200ResponseResultsRURentInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsRURentInner]**](MovieWatchProviders200ResponseResultsRURentInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsRUFlatrateInner]**](MovieWatchProviders200ResponseResultsRUFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_ru import MovieWatchProviders200ResponseResultsRU

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsRU from a JSON string
movie_watch_providers200_response_results_ru_instance = MovieWatchProviders200ResponseResultsRU.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsRU.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_ru_dict = movie_watch_providers200_response_results_ru_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsRU from a dict
movie_watch_providers200_response_results_ru_from_dict = MovieWatchProviders200ResponseResultsRU.from_dict(movie_watch_providers200_response_results_ru_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



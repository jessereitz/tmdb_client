# MovieWatchProviders200ResponseResultsSA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsSAFlatrateInner]**](MovieWatchProviders200ResponseResultsSAFlatrateInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsAERentInner]**](MovieWatchProviders200ResponseResultsAERentInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsAERentInner]**](MovieWatchProviders200ResponseResultsAERentInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_sa import MovieWatchProviders200ResponseResultsSA

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsSA from a JSON string
movie_watch_providers200_response_results_sa_instance = MovieWatchProviders200ResponseResultsSA.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsSA.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_sa_dict = movie_watch_providers200_response_results_sa_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsSA from a dict
movie_watch_providers200_response_results_sa_from_dict = MovieWatchProviders200ResponseResultsSA.from_dict(movie_watch_providers200_response_results_sa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MovieWatchProviders200ResponseResultsPS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_ps import MovieWatchProviders200ResponseResultsPS

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsPS from a JSON string
movie_watch_providers200_response_results_ps_instance = MovieWatchProviders200ResponseResultsPS.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsPS.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_ps_dict = movie_watch_providers200_response_results_ps_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsPS from a dict
movie_watch_providers200_response_results_ps_from_dict = MovieWatchProviders200ResponseResultsPS.from_dict(movie_watch_providers200_response_results_ps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



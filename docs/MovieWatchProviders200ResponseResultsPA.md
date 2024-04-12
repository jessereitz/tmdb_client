# MovieWatchProviders200ResponseResultsPA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_pa import MovieWatchProviders200ResponseResultsPA

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsPA from a JSON string
movie_watch_providers200_response_results_pa_instance = MovieWatchProviders200ResponseResultsPA.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsPA.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_pa_dict = movie_watch_providers200_response_results_pa_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsPA from a dict
movie_watch_providers200_response_results_pa_from_dict = MovieWatchProviders200ResponseResultsPA.from_dict(movie_watch_providers200_response_results_pa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



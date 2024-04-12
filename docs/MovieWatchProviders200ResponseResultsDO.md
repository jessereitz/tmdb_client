# MovieWatchProviders200ResponseResultsDO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_do import MovieWatchProviders200ResponseResultsDO

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsDO from a JSON string
movie_watch_providers200_response_results_do_instance = MovieWatchProviders200ResponseResultsDO.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsDO.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_do_dict = movie_watch_providers200_response_results_do_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsDO from a dict
movie_watch_providers200_response_results_do_from_dict = MovieWatchProviders200ResponseResultsDO.from_dict(movie_watch_providers200_response_results_do_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MovieWatchProviders200ResponseResultsLI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsLIFlatrateInner]**](MovieWatchProviders200ResponseResultsLIFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_li import MovieWatchProviders200ResponseResultsLI

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsLI from a JSON string
movie_watch_providers200_response_results_li_instance = MovieWatchProviders200ResponseResultsLI.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsLI.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_li_dict = movie_watch_providers200_response_results_li_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsLI from a dict
movie_watch_providers200_response_results_li_from_dict = MovieWatchProviders200ResponseResultsLI.from_dict(movie_watch_providers200_response_results_li_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



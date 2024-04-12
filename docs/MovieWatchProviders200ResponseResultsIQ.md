# MovieWatchProviders200ResponseResultsIQ


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_iq import MovieWatchProviders200ResponseResultsIQ

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsIQ from a JSON string
movie_watch_providers200_response_results_iq_instance = MovieWatchProviders200ResponseResultsIQ.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsIQ.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_iq_dict = movie_watch_providers200_response_results_iq_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsIQ from a dict
movie_watch_providers200_response_results_iq_from_dict = MovieWatchProviders200ResponseResultsIQ.from_dict(movie_watch_providers200_response_results_iq_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



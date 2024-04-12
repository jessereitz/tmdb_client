# MovieWatchProviders200ResponseResultsSM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsLIFlatrateInner]**](MovieWatchProviders200ResponseResultsLIFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_sm import MovieWatchProviders200ResponseResultsSM

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsSM from a JSON string
movie_watch_providers200_response_results_sm_instance = MovieWatchProviders200ResponseResultsSM.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsSM.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_sm_dict = movie_watch_providers200_response_results_sm_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsSM from a dict
movie_watch_providers200_response_results_sm_from_dict = MovieWatchProviders200ResponseResultsSM.from_dict(movie_watch_providers200_response_results_sm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MovieWatchProviders200ResponseResultsSI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsALBuyInner]**](MovieWatchProviders200ResponseResultsALBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_si import MovieWatchProviders200ResponseResultsSI

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsSI from a JSON string
movie_watch_providers200_response_results_si_instance = MovieWatchProviders200ResponseResultsSI.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsSI.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_si_dict = movie_watch_providers200_response_results_si_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsSI from a dict
movie_watch_providers200_response_results_si_from_dict = MovieWatchProviders200ResponseResultsSI.from_dict(movie_watch_providers200_response_results_si_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



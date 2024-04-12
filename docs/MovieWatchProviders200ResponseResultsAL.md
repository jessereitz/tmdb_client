# MovieWatchProviders200ResponseResultsAL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsALBuyInner]**](MovieWatchProviders200ResponseResultsALBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_al import MovieWatchProviders200ResponseResultsAL

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsAL from a JSON string
movie_watch_providers200_response_results_al_instance = MovieWatchProviders200ResponseResultsAL.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsAL.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_al_dict = movie_watch_providers200_response_results_al_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsAL from a dict
movie_watch_providers200_response_results_al_from_dict = MovieWatchProviders200ResponseResultsAL.from_dict(movie_watch_providers200_response_results_al_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



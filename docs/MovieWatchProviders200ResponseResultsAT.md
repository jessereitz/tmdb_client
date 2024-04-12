# MovieWatchProviders200ResponseResultsAT


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsATFlatrateInner]**](MovieWatchProviders200ResponseResultsATFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsATBuyInner]**](MovieWatchProviders200ResponseResultsATBuyInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsATBuyInner]**](MovieWatchProviders200ResponseResultsATBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_at import MovieWatchProviders200ResponseResultsAT

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsAT from a JSON string
movie_watch_providers200_response_results_at_instance = MovieWatchProviders200ResponseResultsAT.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsAT.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_at_dict = movie_watch_providers200_response_results_at_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsAT from a dict
movie_watch_providers200_response_results_at_from_dict = MovieWatchProviders200ResponseResultsAT.from_dict(movie_watch_providers200_response_results_at_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



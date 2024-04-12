# MovieWatchProviders200ResponseResultsIS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsCLBuyInner]**](MovieWatchProviders200ResponseResultsCLBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsBEFlatrateInner]**](MovieWatchProviders200ResponseResultsBEFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_is import MovieWatchProviders200ResponseResultsIS

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsIS from a JSON string
movie_watch_providers200_response_results_is_instance = MovieWatchProviders200ResponseResultsIS.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsIS.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_is_dict = movie_watch_providers200_response_results_is_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsIS from a dict
movie_watch_providers200_response_results_is_from_dict = MovieWatchProviders200ResponseResultsIS.from_dict(movie_watch_providers200_response_results_is_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



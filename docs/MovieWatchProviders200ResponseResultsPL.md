# MovieWatchProviders200ResponseResultsPL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsAERentInner]**](MovieWatchProviders200ResponseResultsAERentInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsPLFlatrateInner]**](MovieWatchProviders200ResponseResultsPLFlatrateInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsAERentInner]**](MovieWatchProviders200ResponseResultsAERentInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_pl import MovieWatchProviders200ResponseResultsPL

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsPL from a JSON string
movie_watch_providers200_response_results_pl_instance = MovieWatchProviders200ResponseResultsPL.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsPL.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_pl_dict = movie_watch_providers200_response_results_pl_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsPL from a dict
movie_watch_providers200_response_results_pl_from_dict = MovieWatchProviders200ResponseResultsPL.from_dict(movie_watch_providers200_response_results_pl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



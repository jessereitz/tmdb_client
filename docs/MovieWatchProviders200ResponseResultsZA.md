# MovieWatchProviders200ResponseResultsZA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsBGRentInner]**](MovieWatchProviders200ResponseResultsBGRentInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsBGRentInner]**](MovieWatchProviders200ResponseResultsBGRentInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_za import MovieWatchProviders200ResponseResultsZA

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsZA from a JSON string
movie_watch_providers200_response_results_za_instance = MovieWatchProviders200ResponseResultsZA.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsZA.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_za_dict = movie_watch_providers200_response_results_za_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsZA from a dict
movie_watch_providers200_response_results_za_from_dict = MovieWatchProviders200ResponseResultsZA.from_dict(movie_watch_providers200_response_results_za_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



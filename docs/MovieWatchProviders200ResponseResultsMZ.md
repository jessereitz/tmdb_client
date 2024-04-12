# MovieWatchProviders200ResponseResultsMZ


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsMZRentInner]**](MovieWatchProviders200ResponseResultsMZRentInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsMZRentInner]**](MovieWatchProviders200ResponseResultsMZRentInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_mz import MovieWatchProviders200ResponseResultsMZ

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsMZ from a JSON string
movie_watch_providers200_response_results_mz_instance = MovieWatchProviders200ResponseResultsMZ.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsMZ.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_mz_dict = movie_watch_providers200_response_results_mz_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsMZ from a dict
movie_watch_providers200_response_results_mz_from_dict = MovieWatchProviders200ResponseResultsMZ.from_dict(movie_watch_providers200_response_results_mz_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



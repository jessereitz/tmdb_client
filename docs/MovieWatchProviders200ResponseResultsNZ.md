# MovieWatchProviders200ResponseResultsNZ


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsDEBuyInner]**](MovieWatchProviders200ResponseResultsDEBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_nz import MovieWatchProviders200ResponseResultsNZ

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsNZ from a JSON string
movie_watch_providers200_response_results_nz_instance = MovieWatchProviders200ResponseResultsNZ.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsNZ.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_nz_dict = movie_watch_providers200_response_results_nz_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsNZ from a dict
movie_watch_providers200_response_results_nz_from_dict = MovieWatchProviders200ResponseResultsNZ.from_dict(movie_watch_providers200_response_results_nz_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



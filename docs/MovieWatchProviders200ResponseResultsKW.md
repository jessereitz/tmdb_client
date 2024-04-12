# MovieWatchProviders200ResponseResultsKW


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsBHBuyInner]**](MovieWatchProviders200ResponseResultsBHBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_kw import MovieWatchProviders200ResponseResultsKW

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsKW from a JSON string
movie_watch_providers200_response_results_kw_instance = MovieWatchProviders200ResponseResultsKW.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsKW.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_kw_dict = movie_watch_providers200_response_results_kw_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsKW from a dict
movie_watch_providers200_response_results_kw_from_dict = MovieWatchProviders200ResponseResultsKW.from_dict(movie_watch_providers200_response_results_kw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



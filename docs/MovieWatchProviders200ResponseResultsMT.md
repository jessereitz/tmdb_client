# MovieWatchProviders200ResponseResultsMT


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsALBuyInner]**](MovieWatchProviders200ResponseResultsALBuyInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsALBuyInner]**](MovieWatchProviders200ResponseResultsALBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_mt import MovieWatchProviders200ResponseResultsMT

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsMT from a JSON string
movie_watch_providers200_response_results_mt_instance = MovieWatchProviders200ResponseResultsMT.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsMT.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_mt_dict = movie_watch_providers200_response_results_mt_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsMT from a dict
movie_watch_providers200_response_results_mt_from_dict = MovieWatchProviders200ResponseResultsMT.from_dict(movie_watch_providers200_response_results_mt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



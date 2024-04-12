# MovieWatchProviders200ResponseResultsES


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsDEBuyInner]**](MovieWatchProviders200ResponseResultsDEBuyInner.md) |  | [optional] 
**ads** | [**List[MovieWatchProviders200ResponseResultsESAdsInner]**](MovieWatchProviders200ResponseResultsESAdsInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsDEBuyInner]**](MovieWatchProviders200ResponseResultsDEBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_es import MovieWatchProviders200ResponseResultsES

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsES from a JSON string
movie_watch_providers200_response_results_es_instance = MovieWatchProviders200ResponseResultsES.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsES.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_es_dict = movie_watch_providers200_response_results_es_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsES from a dict
movie_watch_providers200_response_results_es_from_dict = MovieWatchProviders200ResponseResultsES.from_dict(movie_watch_providers200_response_results_es_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



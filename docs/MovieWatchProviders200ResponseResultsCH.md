# MovieWatchProviders200ResponseResultsCH


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsCHBuyInner]**](MovieWatchProviders200ResponseResultsCHBuyInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsCHBuyInner]**](MovieWatchProviders200ResponseResultsCHBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_ch import MovieWatchProviders200ResponseResultsCH

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsCH from a JSON string
movie_watch_providers200_response_results_ch_instance = MovieWatchProviders200ResponseResultsCH.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsCH.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_ch_dict = movie_watch_providers200_response_results_ch_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsCH from a dict
movie_watch_providers200_response_results_ch_from_dict = MovieWatchProviders200ResponseResultsCH.from_dict(movie_watch_providers200_response_results_ch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



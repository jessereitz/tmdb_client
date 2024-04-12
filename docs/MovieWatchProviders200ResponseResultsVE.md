# MovieWatchProviders200ResponseResultsVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsCOBuyInner]**](MovieWatchProviders200ResponseResultsCOBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsARFlatrateInner]**](MovieWatchProviders200ResponseResultsARFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsCOBuyInner]**](MovieWatchProviders200ResponseResultsCOBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_ve import MovieWatchProviders200ResponseResultsVE

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsVE from a JSON string
movie_watch_providers200_response_results_ve_instance = MovieWatchProviders200ResponseResultsVE.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsVE.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_ve_dict = movie_watch_providers200_response_results_ve_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsVE from a dict
movie_watch_providers200_response_results_ve_from_dict = MovieWatchProviders200ResponseResultsVE.from_dict(movie_watch_providers200_response_results_ve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



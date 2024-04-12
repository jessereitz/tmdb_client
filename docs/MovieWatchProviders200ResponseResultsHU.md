# MovieWatchProviders200ResponseResultsHU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsARFlatrateInner]**](MovieWatchProviders200ResponseResultsARFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsCZBuyInner]**](MovieWatchProviders200ResponseResultsCZBuyInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsCZBuyInner]**](MovieWatchProviders200ResponseResultsCZBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_hu import MovieWatchProviders200ResponseResultsHU

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsHU from a JSON string
movie_watch_providers200_response_results_hu_instance = MovieWatchProviders200ResponseResultsHU.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsHU.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_hu_dict = movie_watch_providers200_response_results_hu_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsHU from a dict
movie_watch_providers200_response_results_hu_from_dict = MovieWatchProviders200ResponseResultsHU.from_dict(movie_watch_providers200_response_results_hu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



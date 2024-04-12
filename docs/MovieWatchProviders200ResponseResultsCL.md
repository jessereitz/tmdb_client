# MovieWatchProviders200ResponseResultsCL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsCLBuyInner]**](MovieWatchProviders200ResponseResultsCLBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsARFlatrateInner]**](MovieWatchProviders200ResponseResultsARFlatrateInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsCLBuyInner]**](MovieWatchProviders200ResponseResultsCLBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_cl import MovieWatchProviders200ResponseResultsCL

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsCL from a JSON string
movie_watch_providers200_response_results_cl_instance = MovieWatchProviders200ResponseResultsCL.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsCL.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_cl_dict = movie_watch_providers200_response_results_cl_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsCL from a dict
movie_watch_providers200_response_results_cl_from_dict = MovieWatchProviders200ResponseResultsCL.from_dict(movie_watch_providers200_response_results_cl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



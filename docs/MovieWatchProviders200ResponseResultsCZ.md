# MovieWatchProviders200ResponseResultsCZ


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsCZRentInner]**](MovieWatchProviders200ResponseResultsCZRentInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsCZBuyInner]**](MovieWatchProviders200ResponseResultsCZBuyInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_cz import MovieWatchProviders200ResponseResultsCZ

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsCZ from a JSON string
movie_watch_providers200_response_results_cz_instance = MovieWatchProviders200ResponseResultsCZ.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsCZ.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_cz_dict = movie_watch_providers200_response_results_cz_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsCZ from a dict
movie_watch_providers200_response_results_cz_from_dict = MovieWatchProviders200ResponseResultsCZ.from_dict(movie_watch_providers200_response_results_cz_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



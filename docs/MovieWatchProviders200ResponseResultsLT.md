# MovieWatchProviders200ResponseResultsLT


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsLTRentInner]**](MovieWatchProviders200ResponseResultsLTRentInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsCZBuyInner]**](MovieWatchProviders200ResponseResultsCZBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_lt import MovieWatchProviders200ResponseResultsLT

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsLT from a JSON string
movie_watch_providers200_response_results_lt_instance = MovieWatchProviders200ResponseResultsLT.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsLT.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_lt_dict = movie_watch_providers200_response_results_lt_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsLT from a dict
movie_watch_providers200_response_results_lt_from_dict = MovieWatchProviders200ResponseResultsLT.from_dict(movie_watch_providers200_response_results_lt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



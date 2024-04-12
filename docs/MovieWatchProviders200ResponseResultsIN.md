# MovieWatchProviders200ResponseResultsIN


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsINRentInner]**](MovieWatchProviders200ResponseResultsINRentInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsINRentInner]**](MovieWatchProviders200ResponseResultsINRentInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_in import MovieWatchProviders200ResponseResultsIN

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsIN from a JSON string
movie_watch_providers200_response_results_in_instance = MovieWatchProviders200ResponseResultsIN.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsIN.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_in_dict = movie_watch_providers200_response_results_in_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsIN from a dict
movie_watch_providers200_response_results_in_from_dict = MovieWatchProviders200ResponseResultsIN.from_dict(movie_watch_providers200_response_results_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MovieWatchProviders200ResponseResultsAE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAEFlatrateInner]**](MovieWatchProviders200ResponseResultsAEFlatrateInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsAERentInner]**](MovieWatchProviders200ResponseResultsAERentInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsAERentInner]**](MovieWatchProviders200ResponseResultsAERentInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_ae import MovieWatchProviders200ResponseResultsAE

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsAE from a JSON string
movie_watch_providers200_response_results_ae_instance = MovieWatchProviders200ResponseResultsAE.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsAE.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_ae_dict = movie_watch_providers200_response_results_ae_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsAE from a dict
movie_watch_providers200_response_results_ae_from_dict = MovieWatchProviders200ResponseResultsAE.from_dict(movie_watch_providers200_response_results_ae_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MovieWatchProviders200ResponseResultsCA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsCARentInner]**](MovieWatchProviders200ResponseResultsCARentInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsBERentInner]**](MovieWatchProviders200ResponseResultsBERentInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsCAFlatrateInner]**](MovieWatchProviders200ResponseResultsCAFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_ca import MovieWatchProviders200ResponseResultsCA

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsCA from a JSON string
movie_watch_providers200_response_results_ca_instance = MovieWatchProviders200ResponseResultsCA.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsCA.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_ca_dict = movie_watch_providers200_response_results_ca_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsCA from a dict
movie_watch_providers200_response_results_ca_from_dict = MovieWatchProviders200ResponseResultsCA.from_dict(movie_watch_providers200_response_results_ca_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



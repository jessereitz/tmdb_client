# MovieWatchProviders200ResponseResultsBE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsBERentInner]**](MovieWatchProviders200ResponseResultsBERentInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsBEFlatrateInner]**](MovieWatchProviders200ResponseResultsBEFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsBERentInner]**](MovieWatchProviders200ResponseResultsBERentInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_be import MovieWatchProviders200ResponseResultsBE

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsBE from a JSON string
movie_watch_providers200_response_results_be_instance = MovieWatchProviders200ResponseResultsBE.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsBE.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_be_dict = movie_watch_providers200_response_results_be_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsBE from a dict
movie_watch_providers200_response_results_be_from_dict = MovieWatchProviders200ResponseResultsBE.from_dict(movie_watch_providers200_response_results_be_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



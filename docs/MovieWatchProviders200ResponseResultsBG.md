# MovieWatchProviders200ResponseResultsBG


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsBGRentInner]**](MovieWatchProviders200ResponseResultsBGRentInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsBGRentInner]**](MovieWatchProviders200ResponseResultsBGRentInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_bg import MovieWatchProviders200ResponseResultsBG

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsBG from a JSON string
movie_watch_providers200_response_results_bg_instance = MovieWatchProviders200ResponseResultsBG.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsBG.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_bg_dict = movie_watch_providers200_response_results_bg_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsBG from a dict
movie_watch_providers200_response_results_bg_from_dict = MovieWatchProviders200ResponseResultsBG.from_dict(movie_watch_providers200_response_results_bg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



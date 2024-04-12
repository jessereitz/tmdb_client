# MovieWatchProviders200ResponseResultsUG


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsMZRentInner]**](MovieWatchProviders200ResponseResultsMZRentInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsMZRentInner]**](MovieWatchProviders200ResponseResultsMZRentInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_ug import MovieWatchProviders200ResponseResultsUG

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsUG from a JSON string
movie_watch_providers200_response_results_ug_instance = MovieWatchProviders200ResponseResultsUG.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsUG.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_ug_dict = movie_watch_providers200_response_results_ug_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsUG from a dict
movie_watch_providers200_response_results_ug_from_dict = MovieWatchProviders200ResponseResultsUG.from_dict(movie_watch_providers200_response_results_ug_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



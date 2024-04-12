# MovieWatchProviders200ResponseResultsGR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsBGRentInner]**](MovieWatchProviders200ResponseResultsBGRentInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsBGRentInner]**](MovieWatchProviders200ResponseResultsBGRentInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_gr import MovieWatchProviders200ResponseResultsGR

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsGR from a JSON string
movie_watch_providers200_response_results_gr_instance = MovieWatchProviders200ResponseResultsGR.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsGR.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_gr_dict = movie_watch_providers200_response_results_gr_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsGR from a dict
movie_watch_providers200_response_results_gr_from_dict = MovieWatchProviders200ResponseResultsGR.from_dict(movie_watch_providers200_response_results_gr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



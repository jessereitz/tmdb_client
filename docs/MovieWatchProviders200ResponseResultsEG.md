# MovieWatchProviders200ResponseResultsEG


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsBGRentInner]**](MovieWatchProviders200ResponseResultsBGRentInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsBGRentInner]**](MovieWatchProviders200ResponseResultsBGRentInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_eg import MovieWatchProviders200ResponseResultsEG

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsEG from a JSON string
movie_watch_providers200_response_results_eg_instance = MovieWatchProviders200ResponseResultsEG.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsEG.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_eg_dict = movie_watch_providers200_response_results_eg_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsEG from a dict
movie_watch_providers200_response_results_eg_from_dict = MovieWatchProviders200ResponseResultsEG.from_dict(movie_watch_providers200_response_results_eg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



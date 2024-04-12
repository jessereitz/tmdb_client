# MovieWatchProviders200ResponseResultsFR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsFRRentInner]**](MovieWatchProviders200ResponseResultsFRRentInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsFRRentInner]**](MovieWatchProviders200ResponseResultsFRRentInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_fr import MovieWatchProviders200ResponseResultsFR

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsFR from a JSON string
movie_watch_providers200_response_results_fr_instance = MovieWatchProviders200ResponseResultsFR.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsFR.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_fr_dict = movie_watch_providers200_response_results_fr_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsFR from a dict
movie_watch_providers200_response_results_fr_from_dict = MovieWatchProviders200ResponseResultsFR.from_dict(movie_watch_providers200_response_results_fr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



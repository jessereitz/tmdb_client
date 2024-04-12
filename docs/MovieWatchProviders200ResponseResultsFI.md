# MovieWatchProviders200ResponseResultsFI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsBEFlatrateInner]**](MovieWatchProviders200ResponseResultsBEFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsAUBuyInner]**](MovieWatchProviders200ResponseResultsAUBuyInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsAUBuyInner]**](MovieWatchProviders200ResponseResultsAUBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_fi import MovieWatchProviders200ResponseResultsFI

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsFI from a JSON string
movie_watch_providers200_response_results_fi_instance = MovieWatchProviders200ResponseResultsFI.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsFI.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_fi_dict = movie_watch_providers200_response_results_fi_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsFI from a dict
movie_watch_providers200_response_results_fi_from_dict = MovieWatchProviders200ResponseResultsFI.from_dict(movie_watch_providers200_response_results_fi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



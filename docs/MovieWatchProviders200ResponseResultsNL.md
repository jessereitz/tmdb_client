# MovieWatchProviders200ResponseResultsNL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsNLBuyInner]**](MovieWatchProviders200ResponseResultsNLBuyInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsNLBuyInner]**](MovieWatchProviders200ResponseResultsNLBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsBEFlatrateInner]**](MovieWatchProviders200ResponseResultsBEFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_nl import MovieWatchProviders200ResponseResultsNL

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsNL from a JSON string
movie_watch_providers200_response_results_nl_instance = MovieWatchProviders200ResponseResultsNL.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsNL.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_nl_dict = movie_watch_providers200_response_results_nl_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsNL from a dict
movie_watch_providers200_response_results_nl_from_dict = MovieWatchProviders200ResponseResultsNL.from_dict(movie_watch_providers200_response_results_nl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MovieWatchProviders200ResponseResultsEE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsCZBuyInner]**](MovieWatchProviders200ResponseResultsCZBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsCLBuyInner]**](MovieWatchProviders200ResponseResultsCLBuyInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_ee import MovieWatchProviders200ResponseResultsEE

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsEE from a JSON string
movie_watch_providers200_response_results_ee_instance = MovieWatchProviders200ResponseResultsEE.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsEE.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_ee_dict = movie_watch_providers200_response_results_ee_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsEE from a dict
movie_watch_providers200_response_results_ee_from_dict = MovieWatchProviders200ResponseResultsEE.from_dict(movie_watch_providers200_response_results_ee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



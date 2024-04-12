# MovieWatchProviders200ResponseResultsGB


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsBEFlatrateInner]**](MovieWatchProviders200ResponseResultsBEFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsGBBuyInner]**](MovieWatchProviders200ResponseResultsGBBuyInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsGBBuyInner]**](MovieWatchProviders200ResponseResultsGBBuyInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_gb import MovieWatchProviders200ResponseResultsGB

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsGB from a JSON string
movie_watch_providers200_response_results_gb_instance = MovieWatchProviders200ResponseResultsGB.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsGB.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_gb_dict = movie_watch_providers200_response_results_gb_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsGB from a dict
movie_watch_providers200_response_results_gb_from_dict = MovieWatchProviders200ResponseResultsGB.from_dict(movie_watch_providers200_response_results_gb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



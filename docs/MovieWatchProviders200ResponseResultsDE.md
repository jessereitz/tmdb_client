# MovieWatchProviders200ResponseResultsDE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsATFlatrateInner]**](MovieWatchProviders200ResponseResultsATFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsDEBuyInner]**](MovieWatchProviders200ResponseResultsDEBuyInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsDEBuyInner]**](MovieWatchProviders200ResponseResultsDEBuyInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_de import MovieWatchProviders200ResponseResultsDE

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsDE from a JSON string
movie_watch_providers200_response_results_de_instance = MovieWatchProviders200ResponseResultsDE.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsDE.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_de_dict = movie_watch_providers200_response_results_de_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsDE from a dict
movie_watch_providers200_response_results_de_from_dict = MovieWatchProviders200ResponseResultsDE.from_dict(movie_watch_providers200_response_results_de_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



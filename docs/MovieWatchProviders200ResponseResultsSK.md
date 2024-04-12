# MovieWatchProviders200ResponseResultsSK


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsCZBuyInner]**](MovieWatchProviders200ResponseResultsCZBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsCZBuyInner]**](MovieWatchProviders200ResponseResultsCZBuyInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_sk import MovieWatchProviders200ResponseResultsSK

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsSK from a JSON string
movie_watch_providers200_response_results_sk_instance = MovieWatchProviders200ResponseResultsSK.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsSK.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_sk_dict = movie_watch_providers200_response_results_sk_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsSK from a dict
movie_watch_providers200_response_results_sk_from_dict = MovieWatchProviders200ResponseResultsSK.from_dict(movie_watch_providers200_response_results_sk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



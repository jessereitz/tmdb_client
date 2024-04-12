# MovieWatchProviders200ResponseResultsIT


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsITBuyInner]**](MovieWatchProviders200ResponseResultsITBuyInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsITBuyInner]**](MovieWatchProviders200ResponseResultsITBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_it import MovieWatchProviders200ResponseResultsIT

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsIT from a JSON string
movie_watch_providers200_response_results_it_instance = MovieWatchProviders200ResponseResultsIT.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsIT.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_it_dict = movie_watch_providers200_response_results_it_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsIT from a dict
movie_watch_providers200_response_results_it_from_dict = MovieWatchProviders200ResponseResultsIT.from_dict(movie_watch_providers200_response_results_it_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MovieWatchProviders200ResponseResultsCO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsCOBuyInner]**](MovieWatchProviders200ResponseResultsCOBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsARFlatrateInner]**](MovieWatchProviders200ResponseResultsARFlatrateInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsCOBuyInner]**](MovieWatchProviders200ResponseResultsCOBuyInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_co import MovieWatchProviders200ResponseResultsCO

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsCO from a JSON string
movie_watch_providers200_response_results_co_instance = MovieWatchProviders200ResponseResultsCO.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsCO.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_co_dict = movie_watch_providers200_response_results_co_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsCO from a dict
movie_watch_providers200_response_results_co_from_dict = MovieWatchProviders200ResponseResultsCO.from_dict(movie_watch_providers200_response_results_co_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MovieWatchProviders200ResponseResultsIE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsDEBuyInner]**](MovieWatchProviders200ResponseResultsDEBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsDEBuyInner]**](MovieWatchProviders200ResponseResultsDEBuyInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_ie import MovieWatchProviders200ResponseResultsIE

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsIE from a JSON string
movie_watch_providers200_response_results_ie_instance = MovieWatchProviders200ResponseResultsIE.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsIE.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_ie_dict = movie_watch_providers200_response_results_ie_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsIE from a dict
movie_watch_providers200_response_results_ie_from_dict = MovieWatchProviders200ResponseResultsIE.from_dict(movie_watch_providers200_response_results_ie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



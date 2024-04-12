# MovieWatchProviders200ResponseResultsJP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsJPFlatrateInner]**](MovieWatchProviders200ResponseResultsJPFlatrateInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsJPRentInner]**](MovieWatchProviders200ResponseResultsJPRentInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsDKRentInner]**](MovieWatchProviders200ResponseResultsDKRentInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_jp import MovieWatchProviders200ResponseResultsJP

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsJP from a JSON string
movie_watch_providers200_response_results_jp_instance = MovieWatchProviders200ResponseResultsJP.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsJP.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_jp_dict = movie_watch_providers200_response_results_jp_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsJP from a dict
movie_watch_providers200_response_results_jp_from_dict = MovieWatchProviders200ResponseResultsJP.from_dict(movie_watch_providers200_response_results_jp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



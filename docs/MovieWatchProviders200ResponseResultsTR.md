# MovieWatchProviders200ResponseResultsTR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsPERentInner]**](MovieWatchProviders200ResponseResultsPERentInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsPLFlatrateInner]**](MovieWatchProviders200ResponseResultsPLFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsPERentInner]**](MovieWatchProviders200ResponseResultsPERentInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_tr import MovieWatchProviders200ResponseResultsTR

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsTR from a JSON string
movie_watch_providers200_response_results_tr_instance = MovieWatchProviders200ResponseResultsTR.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsTR.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_tr_dict = movie_watch_providers200_response_results_tr_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsTR from a dict
movie_watch_providers200_response_results_tr_from_dict = MovieWatchProviders200ResponseResultsTR.from_dict(movie_watch_providers200_response_results_tr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



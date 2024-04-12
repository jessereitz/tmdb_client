# MovieWatchProviders200ResponseResultsPE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsPERentInner]**](MovieWatchProviders200ResponseResultsPERentInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsPERentInner]**](MovieWatchProviders200ResponseResultsPERentInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsARFlatrateInner]**](MovieWatchProviders200ResponseResultsARFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_pe import MovieWatchProviders200ResponseResultsPE

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsPE from a JSON string
movie_watch_providers200_response_results_pe_instance = MovieWatchProviders200ResponseResultsPE.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsPE.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_pe_dict = movie_watch_providers200_response_results_pe_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsPE from a dict
movie_watch_providers200_response_results_pe_from_dict = MovieWatchProviders200ResponseResultsPE.from_dict(movie_watch_providers200_response_results_pe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



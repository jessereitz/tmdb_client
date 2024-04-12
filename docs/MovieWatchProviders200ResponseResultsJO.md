# MovieWatchProviders200ResponseResultsJO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsBHBuyInner]**](MovieWatchProviders200ResponseResultsBHBuyInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_jo import MovieWatchProviders200ResponseResultsJO

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsJO from a JSON string
movie_watch_providers200_response_results_jo_instance = MovieWatchProviders200ResponseResultsJO.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsJO.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_jo_dict = movie_watch_providers200_response_results_jo_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsJO from a dict
movie_watch_providers200_response_results_jo_from_dict = MovieWatchProviders200ResponseResultsJO.from_dict(movie_watch_providers200_response_results_jo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



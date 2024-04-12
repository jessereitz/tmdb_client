# MovieWatchProviders200ResponseResultsOM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsBHBuyInner]**](MovieWatchProviders200ResponseResultsBHBuyInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsBHBuyInner]**](MovieWatchProviders200ResponseResultsBHBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_om import MovieWatchProviders200ResponseResultsOM

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsOM from a JSON string
movie_watch_providers200_response_results_om_instance = MovieWatchProviders200ResponseResultsOM.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsOM.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_om_dict = movie_watch_providers200_response_results_om_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsOM from a dict
movie_watch_providers200_response_results_om_from_dict = MovieWatchProviders200ResponseResultsOM.from_dict(movie_watch_providers200_response_results_om_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



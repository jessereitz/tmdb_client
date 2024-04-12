# MovieWatchProviders200ResponseResultsRS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsALBuyInner]**](MovieWatchProviders200ResponseResultsALBuyInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_rs import MovieWatchProviders200ResponseResultsRS

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsRS from a JSON string
movie_watch_providers200_response_results_rs_instance = MovieWatchProviders200ResponseResultsRS.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsRS.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_rs_dict = movie_watch_providers200_response_results_rs_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsRS from a dict
movie_watch_providers200_response_results_rs_from_dict = MovieWatchProviders200ResponseResultsRS.from_dict(movie_watch_providers200_response_results_rs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



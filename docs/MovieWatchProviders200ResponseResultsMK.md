# MovieWatchProviders200ResponseResultsMK


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsMKFlatrateInner]**](MovieWatchProviders200ResponseResultsMKFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsALBuyInner]**](MovieWatchProviders200ResponseResultsALBuyInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_mk import MovieWatchProviders200ResponseResultsMK

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsMK from a JSON string
movie_watch_providers200_response_results_mk_instance = MovieWatchProviders200ResponseResultsMK.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsMK.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_mk_dict = movie_watch_providers200_response_results_mk_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsMK from a dict
movie_watch_providers200_response_results_mk_from_dict = MovieWatchProviders200ResponseResultsMK.from_dict(movie_watch_providers200_response_results_mk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



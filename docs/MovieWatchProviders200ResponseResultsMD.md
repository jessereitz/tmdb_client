# MovieWatchProviders200ResponseResultsMD


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsBHBuyInner]**](MovieWatchProviders200ResponseResultsBHBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsMDFlatrateInner]**](MovieWatchProviders200ResponseResultsMDFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_md import MovieWatchProviders200ResponseResultsMD

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsMD from a JSON string
movie_watch_providers200_response_results_md_instance = MovieWatchProviders200ResponseResultsMD.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsMD.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_md_dict = movie_watch_providers200_response_results_md_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsMD from a dict
movie_watch_providers200_response_results_md_from_dict = MovieWatchProviders200ResponseResultsMD.from_dict(movie_watch_providers200_response_results_md_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



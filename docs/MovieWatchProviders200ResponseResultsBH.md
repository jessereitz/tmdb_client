# MovieWatchProviders200ResponseResultsBH


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsBHBuyInner]**](MovieWatchProviders200ResponseResultsBHBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_bh import MovieWatchProviders200ResponseResultsBH

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsBH from a JSON string
movie_watch_providers200_response_results_bh_instance = MovieWatchProviders200ResponseResultsBH.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsBH.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_bh_dict = movie_watch_providers200_response_results_bh_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsBH from a dict
movie_watch_providers200_response_results_bh_from_dict = MovieWatchProviders200ResponseResultsBH.from_dict(movie_watch_providers200_response_results_bh_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MovieWatchProviders200ResponseResultsQA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsBHBuyInner]**](MovieWatchProviders200ResponseResultsBHBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_qa import MovieWatchProviders200ResponseResultsQA

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsQA from a JSON string
movie_watch_providers200_response_results_qa_instance = MovieWatchProviders200ResponseResultsQA.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsQA.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_qa_dict = movie_watch_providers200_response_results_qa_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsQA from a dict
movie_watch_providers200_response_results_qa_from_dict = MovieWatchProviders200ResponseResultsQA.from_dict(movie_watch_providers200_response_results_qa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



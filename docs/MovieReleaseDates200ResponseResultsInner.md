# MovieReleaseDates200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_1** | **str** |  | [optional] 
**release_dates** | [**List[MovieReleaseDates200ResponseResultsInnerReleaseDatesInner]**](MovieReleaseDates200ResponseResultsInnerReleaseDatesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_release_dates200_response_results_inner import MovieReleaseDates200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieReleaseDates200ResponseResultsInner from a JSON string
movie_release_dates200_response_results_inner_instance = MovieReleaseDates200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(MovieReleaseDates200ResponseResultsInner.to_json())

# convert the object into a dict
movie_release_dates200_response_results_inner_dict = movie_release_dates200_response_results_inner_instance.to_dict()
# create an instance of MovieReleaseDates200ResponseResultsInner from a dict
movie_release_dates200_response_results_inner_from_dict = MovieReleaseDates200ResponseResultsInner.from_dict(movie_release_dates200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MovieReviews200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** |  | [optional] 
**author_details** | [**MovieReviews200ResponseResultsInnerAuthorDetails**](MovieReviews200ResponseResultsInnerAuthorDetails.md) |  | [optional] 
**content** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.movie_reviews200_response_results_inner import MovieReviews200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieReviews200ResponseResultsInner from a JSON string
movie_reviews200_response_results_inner_instance = MovieReviews200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(MovieReviews200ResponseResultsInner.to_json())

# convert the object into a dict
movie_reviews200_response_results_inner_dict = movie_reviews200_response_results_inner_instance.to_dict()
# create an instance of MovieReviews200ResponseResultsInner from a dict
movie_reviews200_response_results_inner_from_dict = MovieReviews200ResponseResultsInner.from_dict(movie_reviews200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



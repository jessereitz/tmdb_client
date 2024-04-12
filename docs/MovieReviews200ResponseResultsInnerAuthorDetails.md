# MovieReviews200ResponseResultsInnerAuthorDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**avatar_path** | **str** |  | [optional] 
**rating** | **object** |  | [optional] 

## Example

```python
from tmdb_client.models.movie_reviews200_response_results_inner_author_details import MovieReviews200ResponseResultsInnerAuthorDetails

# TODO update the JSON string below
json = "{}"
# create an instance of MovieReviews200ResponseResultsInnerAuthorDetails from a JSON string
movie_reviews200_response_results_inner_author_details_instance = MovieReviews200ResponseResultsInnerAuthorDetails.from_json(json)
# print the JSON string representation of the object
print(MovieReviews200ResponseResultsInnerAuthorDetails.to_json())

# convert the object into a dict
movie_reviews200_response_results_inner_author_details_dict = movie_reviews200_response_results_inner_author_details_instance.to_dict()
# create an instance of MovieReviews200ResponseResultsInnerAuthorDetails from a dict
movie_reviews200_response_results_inner_author_details_from_dict = MovieReviews200ResponseResultsInnerAuthorDetails.from_dict(movie_reviews200_response_results_inner_author_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



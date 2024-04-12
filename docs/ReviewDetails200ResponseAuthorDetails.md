# ReviewDetails200ResponseAuthorDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**avatar_path** | **str** |  | [optional] 
**rating** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.review_details200_response_author_details import ReviewDetails200ResponseAuthorDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewDetails200ResponseAuthorDetails from a JSON string
review_details200_response_author_details_instance = ReviewDetails200ResponseAuthorDetails.from_json(json)
# print the JSON string representation of the object
print(ReviewDetails200ResponseAuthorDetails.to_json())

# convert the object into a dict
review_details200_response_author_details_dict = review_details200_response_author_details_instance.to_dict()
# create an instance of ReviewDetails200ResponseAuthorDetails from a dict
review_details200_response_author_details_from_dict = ReviewDetails200ResponseAuthorDetails.from_dict(review_details200_response_author_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



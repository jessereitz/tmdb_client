# ReviewDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**author** | **str** |  | [optional] 
**author_details** | [**ReviewDetails200ResponseAuthorDetails**](ReviewDetails200ResponseAuthorDetails.md) |  | [optional] 
**content** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**iso_639_1** | **str** |  | [optional] 
**media_id** | **int** |  | [optional] [default to 0]
**media_title** | **str** |  | [optional] 
**media_type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.review_details200_response import ReviewDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewDetails200Response from a JSON string
review_details200_response_instance = ReviewDetails200Response.from_json(json)
# print the JSON string representation of the object
print(ReviewDetails200Response.to_json())

# convert the object into a dict
review_details200_response_dict = review_details200_response_instance.to_dict()
# create an instance of ReviewDetails200Response from a dict
review_details200_response_from_dict = ReviewDetails200Response.from_dict(review_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



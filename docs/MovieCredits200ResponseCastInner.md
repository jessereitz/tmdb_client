# MovieCredits200ResponseCastInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**gender** | **int** |  | [optional] [default to 0]
**id** | **int** |  | [optional] [default to 0]
**known_for_department** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**profile_path** | **str** |  | [optional] 
**cast_id** | **int** |  | [optional] [default to 0]
**character** | **str** |  | [optional] 
**credit_id** | **str** |  | [optional] 
**order** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.movie_credits200_response_cast_inner import MovieCredits200ResponseCastInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieCredits200ResponseCastInner from a JSON string
movie_credits200_response_cast_inner_instance = MovieCredits200ResponseCastInner.from_json(json)
# print the JSON string representation of the object
print(MovieCredits200ResponseCastInner.to_json())

# convert the object into a dict
movie_credits200_response_cast_inner_dict = movie_credits200_response_cast_inner_instance.to_dict()
# create an instance of MovieCredits200ResponseCastInner from a dict
movie_credits200_response_cast_inner_from_dict = MovieCredits200ResponseCastInner.from_dict(movie_credits200_response_cast_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



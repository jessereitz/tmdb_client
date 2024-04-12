# PersonMovieCredits200ResponseCastInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**backdrop_path** | **str** |  | [optional] 
**genre_ids** | **List[int]** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**original_language** | **str** |  | [optional] 
**original_title** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**poster_path** | **str** |  | [optional] 
**release_date** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**video** | **bool** |  | [optional] [default to True]
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]
**character** | **str** |  | [optional] 
**credit_id** | **str** |  | [optional] 
**order** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.person_movie_credits200_response_cast_inner import PersonMovieCredits200ResponseCastInner

# TODO update the JSON string below
json = "{}"
# create an instance of PersonMovieCredits200ResponseCastInner from a JSON string
person_movie_credits200_response_cast_inner_instance = PersonMovieCredits200ResponseCastInner.from_json(json)
# print the JSON string representation of the object
print(PersonMovieCredits200ResponseCastInner.to_json())

# convert the object into a dict
person_movie_credits200_response_cast_inner_dict = person_movie_credits200_response_cast_inner_instance.to_dict()
# create an instance of PersonMovieCredits200ResponseCastInner from a dict
person_movie_credits200_response_cast_inner_from_dict = PersonMovieCredits200ResponseCastInner.from_dict(person_movie_credits200_response_cast_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



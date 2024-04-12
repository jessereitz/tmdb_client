# PersonTvCredits200ResponseCastInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**backdrop_path** | **str** |  | [optional] 
**genre_ids** | **List[int]** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**origin_country** | **List[str]** |  | [optional] 
**original_language** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**poster_path** | **str** |  | [optional] 
**first_air_date** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]
**character** | **str** |  | [optional] 
**credit_id** | **str** |  | [optional] 
**episode_count** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.person_tv_credits200_response_cast_inner import PersonTvCredits200ResponseCastInner

# TODO update the JSON string below
json = "{}"
# create an instance of PersonTvCredits200ResponseCastInner from a JSON string
person_tv_credits200_response_cast_inner_instance = PersonTvCredits200ResponseCastInner.from_json(json)
# print the JSON string representation of the object
print(PersonTvCredits200ResponseCastInner.to_json())

# convert the object into a dict
person_tv_credits200_response_cast_inner_dict = person_tv_credits200_response_cast_inner_instance.to_dict()
# create an instance of PersonTvCredits200ResponseCastInner from a dict
person_tv_credits200_response_cast_inner_from_dict = PersonTvCredits200ResponseCastInner.from_dict(person_tv_credits200_response_cast_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



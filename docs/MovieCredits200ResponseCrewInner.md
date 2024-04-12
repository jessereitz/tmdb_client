# MovieCredits200ResponseCrewInner


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
**credit_id** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**job** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.movie_credits200_response_crew_inner import MovieCredits200ResponseCrewInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieCredits200ResponseCrewInner from a JSON string
movie_credits200_response_crew_inner_instance = MovieCredits200ResponseCrewInner.from_json(json)
# print the JSON string representation of the object
print(MovieCredits200ResponseCrewInner.to_json())

# convert the object into a dict
movie_credits200_response_crew_inner_dict = movie_credits200_response_crew_inner_instance.to_dict()
# create an instance of MovieCredits200ResponseCrewInner from a dict
movie_credits200_response_crew_inner_from_dict = MovieCredits200ResponseCrewInner.from_dict(movie_credits200_response_crew_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



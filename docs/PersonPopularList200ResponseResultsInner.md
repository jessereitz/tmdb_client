# PersonPopularList200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**gender** | **int** |  | [optional] [default to 0]
**id** | **int** |  | [optional] [default to 0]
**known_for** | [**List[PersonPopularList200ResponseResultsInnerKnownForInner]**](PersonPopularList200ResponseResultsInnerKnownForInner.md) |  | [optional] 
**known_for_department** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**profile_path** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.person_popular_list200_response_results_inner import PersonPopularList200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PersonPopularList200ResponseResultsInner from a JSON string
person_popular_list200_response_results_inner_instance = PersonPopularList200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(PersonPopularList200ResponseResultsInner.to_json())

# convert the object into a dict
person_popular_list200_response_results_inner_dict = person_popular_list200_response_results_inner_instance.to_dict()
# create an instance of PersonPopularList200ResponseResultsInner from a dict
person_popular_list200_response_results_inner_from_dict = PersonPopularList200ResponseResultsInner.from_dict(person_popular_list200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



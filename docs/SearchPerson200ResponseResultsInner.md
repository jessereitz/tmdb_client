# SearchPerson200ResponseResultsInner


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
**known_for** | [**List[SearchPerson200ResponseResultsInnerKnownForInner]**](SearchPerson200ResponseResultsInnerKnownForInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.search_person200_response_results_inner import SearchPerson200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchPerson200ResponseResultsInner from a JSON string
search_person200_response_results_inner_instance = SearchPerson200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(SearchPerson200ResponseResultsInner.to_json())

# convert the object into a dict
search_person200_response_results_inner_dict = search_person200_response_results_inner_instance.to_dict()
# create an instance of SearchPerson200ResponseResultsInner from a dict
search_person200_response_results_inner_from_dict = SearchPerson200ResponseResultsInner.from_dict(search_person200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



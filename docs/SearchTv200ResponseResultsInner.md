# SearchTv200ResponseResultsInner


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

## Example

```python
from openapi_client.models.search_tv200_response_results_inner import SearchTv200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTv200ResponseResultsInner from a JSON string
search_tv200_response_results_inner_instance = SearchTv200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(SearchTv200ResponseResultsInner.to_json())

# convert the object into a dict
search_tv200_response_results_inner_dict = search_tv200_response_results_inner_instance.to_dict()
# create an instance of SearchTv200ResponseResultsInner from a dict
search_tv200_response_results_inner_from_dict = SearchTv200ResponseResultsInner.from_dict(search_tv200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



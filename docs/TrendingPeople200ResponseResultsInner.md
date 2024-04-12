# TrendingPeople200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**id** | **int** |  | [optional] [default to 0]
**name** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**media_type** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**gender** | **int** |  | [optional] [default to 0]
**known_for_department** | **str** |  | [optional] 
**profile_path** | **str** |  | [optional] 
**known_for** | [**List[TrendingPeople200ResponseResultsInnerKnownForInner]**](TrendingPeople200ResponseResultsInnerKnownForInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.trending_people200_response_results_inner import TrendingPeople200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TrendingPeople200ResponseResultsInner from a JSON string
trending_people200_response_results_inner_instance = TrendingPeople200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(TrendingPeople200ResponseResultsInner.to_json())

# convert the object into a dict
trending_people200_response_results_inner_dict = trending_people200_response_results_inner_instance.to_dict()
# create an instance of TrendingPeople200ResponseResultsInner from a dict
trending_people200_response_results_inner_from_dict = TrendingPeople200ResponseResultsInner.from_dict(trending_people200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



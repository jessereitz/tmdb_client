# TrendingPeople200ResponseResultsInnerKnownForInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**backdrop_path** | **str** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**title** | **str** |  | [optional] 
**original_language** | **str** |  | [optional] 
**original_title** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**poster_path** | **str** |  | [optional] 
**media_type** | **str** |  | [optional] 
**genre_ids** | **List[int]** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**release_date** | **str** |  | [optional] 
**video** | **bool** |  | [optional] [default to True]
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.trending_people200_response_results_inner_known_for_inner import TrendingPeople200ResponseResultsInnerKnownForInner

# TODO update the JSON string below
json = "{}"
# create an instance of TrendingPeople200ResponseResultsInnerKnownForInner from a JSON string
trending_people200_response_results_inner_known_for_inner_instance = TrendingPeople200ResponseResultsInnerKnownForInner.from_json(json)
# print the JSON string representation of the object
print(TrendingPeople200ResponseResultsInnerKnownForInner.to_json())

# convert the object into a dict
trending_people200_response_results_inner_known_for_inner_dict = trending_people200_response_results_inner_known_for_inner_instance.to_dict()
# create an instance of TrendingPeople200ResponseResultsInnerKnownForInner from a dict
trending_people200_response_results_inner_known_for_inner_from_dict = TrendingPeople200ResponseResultsInnerKnownForInner.from_dict(trending_people200_response_results_inner_known_for_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



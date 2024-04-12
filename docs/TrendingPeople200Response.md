# TrendingPeople200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[TrendingPeople200ResponseResultsInner]**](TrendingPeople200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.trending_people200_response import TrendingPeople200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TrendingPeople200Response from a JSON string
trending_people200_response_instance = TrendingPeople200Response.from_json(json)
# print the JSON string representation of the object
print(TrendingPeople200Response.to_json())

# convert the object into a dict
trending_people200_response_dict = trending_people200_response_instance.to_dict()
# create an instance of TrendingPeople200Response from a dict
trending_people200_response_from_dict = TrendingPeople200Response.from_dict(trending_people200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



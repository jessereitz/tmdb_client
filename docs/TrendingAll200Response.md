# TrendingAll200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[TrendingAll200ResponseResultsInner]**](TrendingAll200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.trending_all200_response import TrendingAll200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TrendingAll200Response from a JSON string
trending_all200_response_instance = TrendingAll200Response.from_json(json)
# print the JSON string representation of the object
print(TrendingAll200Response.to_json())

# convert the object into a dict
trending_all200_response_dict = trending_all200_response_instance.to_dict()
# create an instance of TrendingAll200Response from a dict
trending_all200_response_from_dict = TrendingAll200Response.from_dict(trending_all200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



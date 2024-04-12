# TrendingTv200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[TrendingTv200ResponseResultsInner]**](TrendingTv200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.trending_tv200_response import TrendingTv200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TrendingTv200Response from a JSON string
trending_tv200_response_instance = TrendingTv200Response.from_json(json)
# print the JSON string representation of the object
print(TrendingTv200Response.to_json())

# convert the object into a dict
trending_tv200_response_dict = trending_tv200_response_instance.to_dict()
# create an instance of TrendingTv200Response from a dict
trending_tv200_response_from_dict = TrendingTv200Response.from_dict(trending_tv200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



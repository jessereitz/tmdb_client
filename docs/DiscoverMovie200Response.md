# DiscoverMovie200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[DiscoverMovie200ResponseResultsInner]**](DiscoverMovie200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.discover_movie200_response import DiscoverMovie200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoverMovie200Response from a JSON string
discover_movie200_response_instance = DiscoverMovie200Response.from_json(json)
# print the JSON string representation of the object
print(DiscoverMovie200Response.to_json())

# convert the object into a dict
discover_movie200_response_dict = discover_movie200_response_instance.to_dict()
# create an instance of DiscoverMovie200Response from a dict
discover_movie200_response_from_dict = DiscoverMovie200Response.from_dict(discover_movie200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



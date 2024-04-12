# FindById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movie_results** | [**List[FindById200ResponseMovieResultsInner]**](FindById200ResponseMovieResultsInner.md) |  | [optional] 
**person_results** | **List[str]** |  | [optional] 
**tv_results** | **List[str]** |  | [optional] 
**tv_episode_results** | **List[str]** |  | [optional] 
**tv_season_results** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.find_by_id200_response import FindById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FindById200Response from a JSON string
find_by_id200_response_instance = FindById200Response.from_json(json)
# print the JSON string representation of the object
print(FindById200Response.to_json())

# convert the object into a dict
find_by_id200_response_dict = find_by_id200_response_instance.to_dict()
# create an instance of FindById200Response from a dict
find_by_id200_response_from_dict = FindById200Response.from_dict(find_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



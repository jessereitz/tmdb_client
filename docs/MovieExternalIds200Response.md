# MovieExternalIds200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**imdb_id** | **str** |  | [optional] 
**wikidata_id** | **object** |  | [optional] 
**facebook_id** | **str** |  | [optional] 
**instagram_id** | **object** |  | [optional] 
**twitter_id** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.movie_external_ids200_response import MovieExternalIds200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieExternalIds200Response from a JSON string
movie_external_ids200_response_instance = MovieExternalIds200Response.from_json(json)
# print the JSON string representation of the object
print(MovieExternalIds200Response.to_json())

# convert the object into a dict
movie_external_ids200_response_dict = movie_external_ids200_response_instance.to_dict()
# create an instance of MovieExternalIds200Response from a dict
movie_external_ids200_response_from_dict = MovieExternalIds200Response.from_dict(movie_external_ids200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



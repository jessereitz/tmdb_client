# TvSeriesExternalIds200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**imdb_id** | **str** |  | [optional] 
**freebase_mid** | **str** |  | [optional] 
**freebase_id** | **str** |  | [optional] 
**tvdb_id** | **int** |  | [optional] [default to 0]
**tvrage_id** | **int** |  | [optional] [default to 0]
**wikidata_id** | **str** |  | [optional] 
**facebook_id** | **str** |  | [optional] 
**instagram_id** | **str** |  | [optional] 
**twitter_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tv_series_external_ids200_response import TvSeriesExternalIds200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesExternalIds200Response from a JSON string
tv_series_external_ids200_response_instance = TvSeriesExternalIds200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeriesExternalIds200Response.to_json())

# convert the object into a dict
tv_series_external_ids200_response_dict = tv_series_external_ids200_response_instance.to_dict()
# create an instance of TvSeriesExternalIds200Response from a dict
tv_series_external_ids200_response_from_dict = TvSeriesExternalIds200Response.from_dict(tv_series_external_ids200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



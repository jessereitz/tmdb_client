# TvSeasonExternalIds200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**freebase_mid** | **str** |  | [optional] 
**freebase_id** | **str** |  | [optional] 
**tvdb_id** | **int** |  | [optional] [default to 0]
**tvrage_id** | **object** |  | [optional] 
**wikidata_id** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_external_ids200_response import TvSeasonExternalIds200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonExternalIds200Response from a JSON string
tv_season_external_ids200_response_instance = TvSeasonExternalIds200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeasonExternalIds200Response.to_json())

# convert the object into a dict
tv_season_external_ids200_response_dict = tv_season_external_ids200_response_instance.to_dict()
# create an instance of TvSeasonExternalIds200Response from a dict
tv_season_external_ids200_response_from_dict = TvSeasonExternalIds200Response.from_dict(tv_season_external_ids200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



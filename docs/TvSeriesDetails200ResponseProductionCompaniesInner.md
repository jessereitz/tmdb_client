# TvSeriesDetails200ResponseProductionCompaniesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**logo_path** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**origin_country** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_details200_response_production_companies_inner import TvSeriesDetails200ResponseProductionCompaniesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesDetails200ResponseProductionCompaniesInner from a JSON string
tv_series_details200_response_production_companies_inner_instance = TvSeriesDetails200ResponseProductionCompaniesInner.from_json(json)
# print the JSON string representation of the object
print(TvSeriesDetails200ResponseProductionCompaniesInner.to_json())

# convert the object into a dict
tv_series_details200_response_production_companies_inner_dict = tv_series_details200_response_production_companies_inner_instance.to_dict()
# create an instance of TvSeriesDetails200ResponseProductionCompaniesInner from a dict
tv_series_details200_response_production_companies_inner_from_dict = TvSeriesDetails200ResponseProductionCompaniesInner.from_dict(tv_series_details200_response_production_companies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



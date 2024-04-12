# MovieDetails200ResponseProductionCompaniesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**logo_path** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**origin_country** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.movie_details200_response_production_companies_inner import MovieDetails200ResponseProductionCompaniesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieDetails200ResponseProductionCompaniesInner from a JSON string
movie_details200_response_production_companies_inner_instance = MovieDetails200ResponseProductionCompaniesInner.from_json(json)
# print the JSON string representation of the object
print(MovieDetails200ResponseProductionCompaniesInner.to_json())

# convert the object into a dict
movie_details200_response_production_companies_inner_dict = movie_details200_response_production_companies_inner_instance.to_dict()
# create an instance of MovieDetails200ResponseProductionCompaniesInner from a dict
movie_details200_response_production_companies_inner_from_dict = MovieDetails200ResponseProductionCompaniesInner.from_dict(movie_details200_response_production_companies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



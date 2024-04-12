# MovieDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**backdrop_path** | **str** |  | [optional] 
**belongs_to_collection** | **object** |  | [optional] 
**budget** | **int** |  | [optional] [default to 0]
**genres** | [**List[MovieDetails200ResponseGenresInner]**](MovieDetails200ResponseGenresInner.md) |  | [optional] 
**homepage** | **str** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**imdb_id** | **str** |  | [optional] 
**original_language** | **str** |  | [optional] 
**original_title** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**poster_path** | **str** |  | [optional] 
**production_companies** | [**List[MovieDetails200ResponseProductionCompaniesInner]**](MovieDetails200ResponseProductionCompaniesInner.md) |  | [optional] 
**production_countries** | [**List[MovieDetails200ResponseProductionCountriesInner]**](MovieDetails200ResponseProductionCountriesInner.md) |  | [optional] 
**release_date** | **str** |  | [optional] 
**revenue** | **int** |  | [optional] [default to 0]
**runtime** | **int** |  | [optional] [default to 0]
**spoken_languages** | [**List[MovieDetails200ResponseSpokenLanguagesInner]**](MovieDetails200ResponseSpokenLanguagesInner.md) |  | [optional] 
**status** | **str** |  | [optional] 
**tagline** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**video** | **bool** |  | [optional] [default to True]
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.movie_details200_response import MovieDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieDetails200Response from a JSON string
movie_details200_response_instance = MovieDetails200Response.from_json(json)
# print the JSON string representation of the object
print(MovieDetails200Response.to_json())

# convert the object into a dict
movie_details200_response_dict = movie_details200_response_instance.to_dict()
# create an instance of MovieDetails200Response from a dict
movie_details200_response_from_dict = MovieDetails200Response.from_dict(movie_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



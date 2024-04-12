# MovieLatestId200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**backdrop_path** | **object** |  | [optional] 
**belongs_to_collection** | **object** |  | [optional] 
**budget** | **int** |  | [optional] [default to 0]
**genres** | **List[str]** |  | [optional] 
**homepage** | **str** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**imdb_id** | **object** |  | [optional] 
**original_language** | **str** |  | [optional] 
**original_title** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**popularity** | **int** |  | [optional] [default to 0]
**poster_path** | **object** |  | [optional] 
**production_companies** | **List[str]** |  | [optional] 
**production_countries** | **List[str]** |  | [optional] 
**release_date** | **str** |  | [optional] 
**revenue** | **int** |  | [optional] [default to 0]
**runtime** | **int** |  | [optional] [default to 0]
**spoken_languages** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 
**tagline** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**video** | **bool** |  | [optional] [default to True]
**vote_average** | **int** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.movie_latest_id200_response import MovieLatestId200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieLatestId200Response from a JSON string
movie_latest_id200_response_instance = MovieLatestId200Response.from_json(json)
# print the JSON string representation of the object
print(MovieLatestId200Response.to_json())

# convert the object into a dict
movie_latest_id200_response_dict = movie_latest_id200_response_instance.to_dict()
# create an instance of MovieLatestId200Response from a dict
movie_latest_id200_response_from_dict = MovieLatestId200Response.from_dict(movie_latest_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



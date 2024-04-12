# MovieDetails200ResponseSpokenLanguagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**english_name** | **str** |  | [optional] 
**iso_639_1** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.movie_details200_response_spoken_languages_inner import MovieDetails200ResponseSpokenLanguagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieDetails200ResponseSpokenLanguagesInner from a JSON string
movie_details200_response_spoken_languages_inner_instance = MovieDetails200ResponseSpokenLanguagesInner.from_json(json)
# print the JSON string representation of the object
print(MovieDetails200ResponseSpokenLanguagesInner.to_json())

# convert the object into a dict
movie_details200_response_spoken_languages_inner_dict = movie_details200_response_spoken_languages_inner_instance.to_dict()
# create an instance of MovieDetails200ResponseSpokenLanguagesInner from a dict
movie_details200_response_spoken_languages_inner_from_dict = MovieDetails200ResponseSpokenLanguagesInner.from_dict(movie_details200_response_spoken_languages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



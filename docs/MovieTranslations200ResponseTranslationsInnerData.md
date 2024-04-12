# MovieTranslations200ResponseTranslationsInnerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**homepage** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**runtime** | **int** |  | [optional] [default to 0]
**tagline** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.movie_translations200_response_translations_inner_data import MovieTranslations200ResponseTranslationsInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of MovieTranslations200ResponseTranslationsInnerData from a JSON string
movie_translations200_response_translations_inner_data_instance = MovieTranslations200ResponseTranslationsInnerData.from_json(json)
# print the JSON string representation of the object
print(MovieTranslations200ResponseTranslationsInnerData.to_json())

# convert the object into a dict
movie_translations200_response_translations_inner_data_dict = movie_translations200_response_translations_inner_data_instance.to_dict()
# create an instance of MovieTranslations200ResponseTranslationsInnerData from a dict
movie_translations200_response_translations_inner_data_from_dict = MovieTranslations200ResponseTranslationsInnerData.from_dict(movie_translations200_response_translations_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



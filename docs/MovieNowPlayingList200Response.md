# MovieNowPlayingList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dates** | [**MovieNowPlayingList200ResponseDates**](MovieNowPlayingList200ResponseDates.md) |  | [optional] 
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[MovieNowPlayingList200ResponseResultsInner]**](MovieNowPlayingList200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.movie_now_playing_list200_response import MovieNowPlayingList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieNowPlayingList200Response from a JSON string
movie_now_playing_list200_response_instance = MovieNowPlayingList200Response.from_json(json)
# print the JSON string representation of the object
print(MovieNowPlayingList200Response.to_json())

# convert the object into a dict
movie_now_playing_list200_response_dict = movie_now_playing_list200_response_instance.to_dict()
# create an instance of MovieNowPlayingList200Response from a dict
movie_now_playing_list200_response_from_dict = MovieNowPlayingList200Response.from_dict(movie_now_playing_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MovieNowPlayingList200ResponseDates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum** | **str** |  | [optional] 
**minimum** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.movie_now_playing_list200_response_dates import MovieNowPlayingList200ResponseDates

# TODO update the JSON string below
json = "{}"
# create an instance of MovieNowPlayingList200ResponseDates from a JSON string
movie_now_playing_list200_response_dates_instance = MovieNowPlayingList200ResponseDates.from_json(json)
# print the JSON string representation of the object
print(MovieNowPlayingList200ResponseDates.to_json())

# convert the object into a dict
movie_now_playing_list200_response_dates_dict = movie_now_playing_list200_response_dates_instance.to_dict()
# create an instance of MovieNowPlayingList200ResponseDates from a dict
movie_now_playing_list200_response_dates_from_dict = MovieNowPlayingList200ResponseDates.from_dict(movie_now_playing_list200_response_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



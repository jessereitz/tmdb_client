# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_now_playing_list200_response_results_inner import MovieNowPlayingList200ResponseResultsInner

class TestMovieNowPlayingList200ResponseResultsInner(unittest.TestCase):
    """MovieNowPlayingList200ResponseResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieNowPlayingList200ResponseResultsInner:
        """Test MovieNowPlayingList200ResponseResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieNowPlayingList200ResponseResultsInner`
        """
        model = MovieNowPlayingList200ResponseResultsInner()
        if include_optional:
            return MovieNowPlayingList200ResponseResultsInner(
                adult = False,
                backdrop_path = '/iJQIbOPm81fPEGKt5BPuZmfnA54.jpg',
                genre_ids = [
                    16
                    ],
                id = 502356,
                original_language = 'en',
                original_title = 'The Super Mario Bros. Movie',
                overview = 'While working underground to fix a water main, Brooklyn plumbers—and brothers—Mario and Luigi are transported down a mysterious pipe and wander into a magical new world. But when the brothers are separated, Mario embarks on an epic quest to find Luigi.',
                popularity = 6572.614,
                poster_path = '/qNBAXBIQlnOThrVvA6mA2B5ggV6.jpg',
                release_date = '2023-04-05',
                title = 'The Super Mario Bros. Movie',
                video = False,
                vote_average = 7.5,
                vote_count = 1456
            )
        else:
            return MovieNowPlayingList200ResponseResultsInner(
        )
        """

    def testMovieNowPlayingList200ResponseResultsInner(self):
        """Test MovieNowPlayingList200ResponseResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

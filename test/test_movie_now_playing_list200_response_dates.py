# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_now_playing_list200_response_dates import MovieNowPlayingList200ResponseDates

class TestMovieNowPlayingList200ResponseDates(unittest.TestCase):
    """MovieNowPlayingList200ResponseDates unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieNowPlayingList200ResponseDates:
        """Test MovieNowPlayingList200ResponseDates
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieNowPlayingList200ResponseDates`
        """
        model = MovieNowPlayingList200ResponseDates()
        if include_optional:
            return MovieNowPlayingList200ResponseDates(
                maximum = '2023-05-03',
                minimum = '2023-03-16'
            )
        else:
            return MovieNowPlayingList200ResponseDates(
        )
        """

    def testMovieNowPlayingList200ResponseDates(self):
        """Test MovieNowPlayingList200ResponseDates"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

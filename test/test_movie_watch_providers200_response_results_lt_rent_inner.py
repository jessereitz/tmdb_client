# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_watch_providers200_response_results_lt_rent_inner import MovieWatchProviders200ResponseResultsLTRentInner

class TestMovieWatchProviders200ResponseResultsLTRentInner(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsLTRentInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsLTRentInner:
        """Test MovieWatchProviders200ResponseResultsLTRentInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsLTRentInner`
        """
        model = MovieWatchProviders200ResponseResultsLTRentInner()
        if include_optional:
            return MovieWatchProviders200ResponseResultsLTRentInner(
                logo_path = '/xTVM8uXT9QocigQ07LE7Irc65W2.jpg',
                provider_id = 553,
                provider_name = 'Telia Play',
                display_priority = 15
            )
        else:
            return MovieWatchProviders200ResponseResultsLTRentInner(
        )
        """

    def testMovieWatchProviders200ResponseResultsLTRentInner(self):
        """Test MovieWatchProviders200ResponseResultsLTRentInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_cz_rent_inner import MovieWatchProviders200ResponseResultsCZRentInner

class TestMovieWatchProviders200ResponseResultsCZRentInner(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsCZRentInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsCZRentInner:
        """Test MovieWatchProviders200ResponseResultsCZRentInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsCZRentInner`
        """
        model = MovieWatchProviders200ResponseResultsCZRentInner()
        if include_optional:
            return MovieWatchProviders200ResponseResultsCZRentInner(
                logo_path = '/wTF37o4jOkQfjnWe41gmeuASYZA.jpg',
                provider_id = 308,
                provider_name = 'O2 TV',
                display_priority = 2
            )
        else:
            return MovieWatchProviders200ResponseResultsCZRentInner(
        )
        """

    def testMovieWatchProviders200ResponseResultsCZRentInner(self):
        """Test MovieWatchProviders200ResponseResultsCZRentInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

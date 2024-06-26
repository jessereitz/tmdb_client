# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_jp_rent_inner import MovieWatchProviders200ResponseResultsJPRentInner

class TestMovieWatchProviders200ResponseResultsJPRentInner(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsJPRentInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsJPRentInner:
        """Test MovieWatchProviders200ResponseResultsJPRentInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsJPRentInner`
        """
        model = MovieWatchProviders200ResponseResultsJPRentInner()
        if include_optional:
            return MovieWatchProviders200ResponseResultsJPRentInner(
                logo_path = '/g8jqHtXJsMlc8B1Gb0Rt8AvUJMn.jpg',
                provider_id = 85,
                provider_name = 'dTV',
                display_priority = 2
            )
        else:
            return MovieWatchProviders200ResponseResultsJPRentInner(
        )
        """

    def testMovieWatchProviders200ResponseResultsJPRentInner(self):
        """Test MovieWatchProviders200ResponseResultsJPRentInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

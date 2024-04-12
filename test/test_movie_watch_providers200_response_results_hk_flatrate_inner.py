# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_watch_providers200_response_results_hk_flatrate_inner import MovieWatchProviders200ResponseResultsHKFlatrateInner

class TestMovieWatchProviders200ResponseResultsHKFlatrateInner(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsHKFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsHKFlatrateInner:
        """Test MovieWatchProviders200ResponseResultsHKFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsHKFlatrateInner`
        """
        model = MovieWatchProviders200ResponseResultsHKFlatrateInner()
        if include_optional:
            return MovieWatchProviders200ResponseResultsHKFlatrateInner(
                logo_path = '/emthp39XA2YScoYL1p0sdbAH2WA.jpg',
                provider_id = 119,
                provider_name = 'Amazon Prime Video',
                display_priority = 7
            )
        else:
            return MovieWatchProviders200ResponseResultsHKFlatrateInner(
        )
        """

    def testMovieWatchProviders200ResponseResultsHKFlatrateInner(self):
        """Test MovieWatchProviders200ResponseResultsHKFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_watch_providers200_response_results_pl_flatrate_inner import MovieWatchProviders200ResponseResultsPLFlatrateInner

class TestMovieWatchProviders200ResponseResultsPLFlatrateInner(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsPLFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsPLFlatrateInner:
        """Test MovieWatchProviders200ResponseResultsPLFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsPLFlatrateInner`
        """
        model = MovieWatchProviders200ResponseResultsPLFlatrateInner()
        if include_optional:
            return MovieWatchProviders200ResponseResultsPLFlatrateInner(
                logo_path = '/emthp39XA2YScoYL1p0sdbAH2WA.jpg',
                provider_id = 119,
                provider_name = 'Amazon Prime Video',
                display_priority = 4
            )
        else:
            return MovieWatchProviders200ResponseResultsPLFlatrateInner(
        )
        """

    def testMovieWatchProviders200ResponseResultsPLFlatrateInner(self):
        """Test MovieWatchProviders200ResponseResultsPLFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

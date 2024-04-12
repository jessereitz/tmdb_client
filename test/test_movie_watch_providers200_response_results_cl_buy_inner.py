# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_watch_providers200_response_results_cl_buy_inner import MovieWatchProviders200ResponseResultsCLBuyInner

class TestMovieWatchProviders200ResponseResultsCLBuyInner(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsCLBuyInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsCLBuyInner:
        """Test MovieWatchProviders200ResponseResultsCLBuyInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsCLBuyInner`
        """
        model = MovieWatchProviders200ResponseResultsCLBuyInner()
        if include_optional:
            return MovieWatchProviders200ResponseResultsCLBuyInner(
                logo_path = '/tbEdFQDwx5LEVr8WpSeXQSIirVq.jpg',
                provider_id = 3,
                provider_name = 'Google Play Movies',
                display_priority = 4
            )
        else:
            return MovieWatchProviders200ResponseResultsCLBuyInner(
        )
        """

    def testMovieWatchProviders200ResponseResultsCLBuyInner(self):
        """Test MovieWatchProviders200ResponseResultsCLBuyInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

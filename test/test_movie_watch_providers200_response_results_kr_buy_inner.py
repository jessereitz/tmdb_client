# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_watch_providers200_response_results_kr_buy_inner import MovieWatchProviders200ResponseResultsKRBuyInner

class TestMovieWatchProviders200ResponseResultsKRBuyInner(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsKRBuyInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsKRBuyInner:
        """Test MovieWatchProviders200ResponseResultsKRBuyInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsKRBuyInner`
        """
        model = MovieWatchProviders200ResponseResultsKRBuyInner()
        if include_optional:
            return MovieWatchProviders200ResponseResultsKRBuyInner(
                logo_path = '/2ioan5BX5L9tz4fIGU93blTeFhv.jpg',
                provider_id = 356,
                provider_name = 'wavve',
                display_priority = 3
            )
        else:
            return MovieWatchProviders200ResponseResultsKRBuyInner(
        )
        """

    def testMovieWatchProviders200ResponseResultsKRBuyInner(self):
        """Test MovieWatchProviders200ResponseResultsKRBuyInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

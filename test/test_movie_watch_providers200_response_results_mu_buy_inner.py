# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_mu_buy_inner import MovieWatchProviders200ResponseResultsMUBuyInner

class TestMovieWatchProviders200ResponseResultsMUBuyInner(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsMUBuyInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsMUBuyInner:
        """Test MovieWatchProviders200ResponseResultsMUBuyInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsMUBuyInner`
        """
        model = MovieWatchProviders200ResponseResultsMUBuyInner()
        if include_optional:
            return MovieWatchProviders200ResponseResultsMUBuyInner(
                logo_path = '/peURlLlr8jggOwK53fJ5wdQl05y.jpg',
                provider_id = 2,
                provider_name = 'Apple TV',
                display_priority = 15
            )
        else:
            return MovieWatchProviders200ResponseResultsMUBuyInner(
        )
        """

    def testMovieWatchProviders200ResponseResultsMUBuyInner(self):
        """Test MovieWatchProviders200ResponseResultsMUBuyInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_cz_buy_inner import MovieWatchProviders200ResponseResultsCZBuyInner

class TestMovieWatchProviders200ResponseResultsCZBuyInner(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsCZBuyInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsCZBuyInner:
        """Test MovieWatchProviders200ResponseResultsCZBuyInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsCZBuyInner`
        """
        model = MovieWatchProviders200ResponseResultsCZBuyInner()
        if include_optional:
            return MovieWatchProviders200ResponseResultsCZBuyInner(
                logo_path = '/peURlLlr8jggOwK53fJ5wdQl05y.jpg',
                provider_id = 2,
                provider_name = 'Apple TV',
                display_priority = 3
            )
        else:
            return MovieWatchProviders200ResponseResultsCZBuyInner(
        )
        """

    def testMovieWatchProviders200ResponseResultsCZBuyInner(self):
        """Test MovieWatchProviders200ResponseResultsCZBuyInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

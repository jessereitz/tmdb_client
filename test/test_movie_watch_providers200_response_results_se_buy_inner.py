# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_watch_providers200_response_results_se_buy_inner import MovieWatchProviders200ResponseResultsSEBuyInner

class TestMovieWatchProviders200ResponseResultsSEBuyInner(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsSEBuyInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsSEBuyInner:
        """Test MovieWatchProviders200ResponseResultsSEBuyInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsSEBuyInner`
        """
        model = MovieWatchProviders200ResponseResultsSEBuyInner()
        if include_optional:
            return MovieWatchProviders200ResponseResultsSEBuyInner(
                logo_path = '/shq88b09gTBYC4hA7K7MUL8Q4zP.jpg',
                provider_id = 68,
                provider_name = 'Microsoft Store',
                display_priority = 7
            )
        else:
            return MovieWatchProviders200ResponseResultsSEBuyInner(
        )
        """

    def testMovieWatchProviders200ResponseResultsSEBuyInner(self):
        """Test MovieWatchProviders200ResponseResultsSEBuyInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

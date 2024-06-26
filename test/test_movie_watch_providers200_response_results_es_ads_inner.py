# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_es_ads_inner import MovieWatchProviders200ResponseResultsESAdsInner

class TestMovieWatchProviders200ResponseResultsESAdsInner(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsESAdsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsESAdsInner:
        """Test MovieWatchProviders200ResponseResultsESAdsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsESAdsInner`
        """
        model = MovieWatchProviders200ResponseResultsESAdsInner()
        if include_optional:
            return MovieWatchProviders200ResponseResultsESAdsInner(
                logo_path = '/5GEbAhFW2S5T8zVc1MNvz00pIzM.jpg',
                provider_id = 35,
                provider_name = 'Rakuten TV',
                display_priority = 11
            )
        else:
            return MovieWatchProviders200ResponseResultsESAdsInner(
        )
        """

    def testMovieWatchProviders200ResponseResultsESAdsInner(self):
        """Test MovieWatchProviders200ResponseResultsESAdsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

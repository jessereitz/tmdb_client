# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_gq import TvSeriesWatchProviders200ResponseResultsGQ

class TestTvSeriesWatchProviders200ResponseResultsGQ(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsGQ unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsGQ:
        """Test TvSeriesWatchProviders200ResponseResultsGQ
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsGQ`
        """
        model = TvSeriesWatchProviders200ResponseResultsGQ()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsGQ(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=GQ',
                flatrate = [
                    tmdb_client.models.tv_series_watch_providers_200_response_results_gh_flatrate_inner.tv_series_watch_providers_200_response_results_GH_flatrate_inner(
                        logo_path = '/okiQZMXnqwv0aD3QDYmu5DBNLce.jpg', 
                        provider_id = 55, 
                        provider_name = 'ShowMax', 
                        display_priority = 11, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsGQ(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsGQ(self):
        """Test TvSeriesWatchProviders200ResponseResultsGQ"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

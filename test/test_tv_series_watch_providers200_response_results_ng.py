# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_ng import TvSeriesWatchProviders200ResponseResultsNG

class TestTvSeriesWatchProviders200ResponseResultsNG(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsNG unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsNG:
        """Test TvSeriesWatchProviders200ResponseResultsNG
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsNG`
        """
        model = TvSeriesWatchProviders200ResponseResultsNG()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsNG(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=NG',
                flatrate = [
                    tmdb_client.models.tv_series_watch_providers_200_response_results_dz_flatrate_inner.tv_series_watch_providers_200_response_results_DZ_flatrate_inner(
                        logo_path = '/okiQZMXnqwv0aD3QDYmu5DBNLce.jpg', 
                        provider_id = 55, 
                        provider_name = 'ShowMax', 
                        display_priority = 27, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsNG(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsNG(self):
        """Test TvSeriesWatchProviders200ResponseResultsNG"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

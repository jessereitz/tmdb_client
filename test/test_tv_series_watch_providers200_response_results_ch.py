# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_ch import TvSeriesWatchProviders200ResponseResultsCH

class TestTvSeriesWatchProviders200ResponseResultsCH(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsCH unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsCH:
        """Test TvSeriesWatchProviders200ResponseResultsCH
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsCH`
        """
        model = TvSeriesWatchProviders200ResponseResultsCH()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsCH(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=CH',
                flatrate = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_ch_flatrate_inner.tv_series_watch_providers_200_response_results_CH_flatrate_inner(
                        logo_path = '/sHP8XLo4Ac4WMbziRyAdRQdb76q.jpg', 
                        provider_id = 210, 
                        provider_name = 'Sky', 
                        display_priority = 7, )
                    ],
                buy = [
                    openapi_client.models.movie_watch_providers_200_response_results_pe_rent_inner.movie_watch_providers_200_response_results_PE_rent_inner(
                        logo_path = '/tbEdFQDwx5LEVr8WpSeXQSIirVq.jpg', 
                        provider_id = 3, 
                        provider_name = 'Google Play Movies', 
                        display_priority = 5, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsCH(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsCH(self):
        """Test TvSeriesWatchProviders200ResponseResultsCH"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
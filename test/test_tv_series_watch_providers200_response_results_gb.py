# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_gb import TvSeriesWatchProviders200ResponseResultsGB

class TestTvSeriesWatchProviders200ResponseResultsGB(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsGB unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsGB:
        """Test TvSeriesWatchProviders200ResponseResultsGB
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsGB`
        """
        model = TvSeriesWatchProviders200ResponseResultsGB()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsGB(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=GB',
                flatrate = [
                    tmdb_client.models.tv_series_watch_providers_200_response_results_gb_flatrate_inner.tv_series_watch_providers_200_response_results_GB_flatrate_inner(
                        logo_path = '/fBHHXKC34ffxAsQvDe0ZJbvmTEQ.jpg', 
                        provider_id = 29, 
                        provider_name = 'Sky Go', 
                        display_priority = 9, )
                    ],
                buy = [
                    tmdb_client.models.movie_watch_providers_200_response_results_gb_buy_inner.movie_watch_providers_200_response_results_GB_buy_inner(
                        logo_path = '/5NyLm42TmCqCMOZFvH4fcoSNKEW.jpg', 
                        provider_id = 10, 
                        provider_name = 'Amazon Video', 
                        display_priority = 4, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsGB(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsGB(self):
        """Test TvSeriesWatchProviders200ResponseResultsGB"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

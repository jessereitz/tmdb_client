# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_au import TvSeriesWatchProviders200ResponseResultsAU

class TestTvSeriesWatchProviders200ResponseResultsAU(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsAU unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsAU:
        """Test TvSeriesWatchProviders200ResponseResultsAU
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsAU`
        """
        model = TvSeriesWatchProviders200ResponseResultsAU()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsAU(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=AU',
                flatrate = [
                    tmdb_client.models.tv_series_watch_providers_200_response_results_au_flatrate_inner.tv_series_watch_providers_200_response_results_AU_flatrate_inner(
                        logo_path = '/d3ixI1no0EpTj2i7u0Sd2DBXVlG.jpg', 
                        provider_id = 385, 
                        provider_name = 'BINGE', 
                        display_priority = 3, )
                    ],
                buy = [
                    tmdb_client.models.movie_watch_providers_200_response_results_au_buy_inner.movie_watch_providers_200_response_results_AU_buy_inner(
                        logo_path = '/peURlLlr8jggOwK53fJ5wdQl05y.jpg', 
                        provider_id = 2, 
                        provider_name = 'Apple TV', 
                        display_priority = 10, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsAU(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsAU(self):
        """Test TvSeriesWatchProviders200ResponseResultsAU"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

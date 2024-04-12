# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_us import TvSeriesWatchProviders200ResponseResultsUS

class TestTvSeriesWatchProviders200ResponseResultsUS(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsUS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsUS:
        """Test TvSeriesWatchProviders200ResponseResultsUS
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsUS`
        """
        model = TvSeriesWatchProviders200ResponseResultsUS()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsUS(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=US',
                free = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_br_flatrate_inner.tv_series_watch_providers_200_response_results_BR_flatrate_inner(
                        logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg', 
                        provider_id = 384, 
                        provider_name = 'HBO Max', 
                        display_priority = 7, )
                    ],
                buy = [
                    openapi_client.models.movie_watch_providers_200_response_results_de_buy_inner.movie_watch_providers_200_response_results_DE_buy_inner(
                        logo_path = '/peURlLlr8jggOwK53fJ5wdQl05y.jpg', 
                        provider_id = 2, 
                        provider_name = 'Apple TV', 
                        display_priority = 4, )
                    ],
                flatrate = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_br_flatrate_inner.tv_series_watch_providers_200_response_results_BR_flatrate_inner(
                        logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg', 
                        provider_id = 384, 
                        provider_name = 'HBO Max', 
                        display_priority = 7, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsUS(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsUS(self):
        """Test TvSeriesWatchProviders200ResponseResultsUS"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_season_watch_providers200_response_results_fr import TvSeasonWatchProviders200ResponseResultsFR

class TestTvSeasonWatchProviders200ResponseResultsFR(unittest.TestCase):
    """TvSeasonWatchProviders200ResponseResultsFR unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeasonWatchProviders200ResponseResultsFR:
        """Test TvSeasonWatchProviders200ResponseResultsFR
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeasonWatchProviders200ResponseResultsFR`
        """
        model = TvSeasonWatchProviders200ResponseResultsFR()
        if include_optional:
            return TvSeasonWatchProviders200ResponseResultsFR(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/season/1/watch?locale=FR',
                flatrate = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_fr_flatrate_inner.tv_series_watch_providers_200_response_results_FR_flatrate_inner(
                        logo_path = '/loOaayvNiLnD0zKl70TO2L5vlAL.jpg', 
                        provider_id = 1870, 
                        provider_name = 'Pass Warner Amazon Channel', 
                        display_priority = 95, )
                    ],
                buy = [
                    openapi_client.models.movie_watch_providers_200_response_results_fr_rent_inner.movie_watch_providers_200_response_results_FR_rent_inner(
                        logo_path = '/peURlLlr8jggOwK53fJ5wdQl05y.jpg', 
                        provider_id = 2, 
                        provider_name = 'Apple TV', 
                        display_priority = 5, )
                    ]
            )
        else:
            return TvSeasonWatchProviders200ResponseResultsFR(
        )
        """

    def testTvSeasonWatchProviders200ResponseResultsFR(self):
        """Test TvSeasonWatchProviders200ResponseResultsFR"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

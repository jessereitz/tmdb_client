# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_season_watch_providers200_response_results_ph import TvSeasonWatchProviders200ResponseResultsPH

class TestTvSeasonWatchProviders200ResponseResultsPH(unittest.TestCase):
    """TvSeasonWatchProviders200ResponseResultsPH unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeasonWatchProviders200ResponseResultsPH:
        """Test TvSeasonWatchProviders200ResponseResultsPH
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeasonWatchProviders200ResponseResultsPH`
        """
        model = TvSeasonWatchProviders200ResponseResultsPH()
        if include_optional:
            return TvSeasonWatchProviders200ResponseResultsPH(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/season/1/watch?locale=PH',
                flatrate = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_ph_flatrate_inner.tv_series_watch_providers_200_response_results_PH_flatrate_inner(
                        logo_path = '/bxdNcDbk1ohVeOMmM3eusAAiTLw.jpg', 
                        provider_id = 425, 
                        provider_name = 'HBO Go', 
                        display_priority = 12, )
                    ]
            )
        else:
            return TvSeasonWatchProviders200ResponseResultsPH(
        )
        """

    def testTvSeasonWatchProviders200ResponseResultsPH(self):
        """Test TvSeasonWatchProviders200ResponseResultsPH"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_season_watch_providers200_response_results_hk import TvSeasonWatchProviders200ResponseResultsHK

class TestTvSeasonWatchProviders200ResponseResultsHK(unittest.TestCase):
    """TvSeasonWatchProviders200ResponseResultsHK unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeasonWatchProviders200ResponseResultsHK:
        """Test TvSeasonWatchProviders200ResponseResultsHK
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeasonWatchProviders200ResponseResultsHK`
        """
        model = TvSeasonWatchProviders200ResponseResultsHK()
        if include_optional:
            return TvSeasonWatchProviders200ResponseResultsHK(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/season/1/watch?locale=HK',
                flatrate = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_hk_flatrate_inner.tv_series_watch_providers_200_response_results_HK_flatrate_inner(
                        logo_path = '/bxdNcDbk1ohVeOMmM3eusAAiTLw.jpg', 
                        provider_id = 425, 
                        provider_name = 'HBO Go', 
                        display_priority = 40, )
                    ]
            )
        else:
            return TvSeasonWatchProviders200ResponseResultsHK(
        )
        """

    def testTvSeasonWatchProviders200ResponseResultsHK(self):
        """Test TvSeasonWatchProviders200ResponseResultsHK"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
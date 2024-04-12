# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_season_watch_providers200_response_results_no import TvSeasonWatchProviders200ResponseResultsNO

class TestTvSeasonWatchProviders200ResponseResultsNO(unittest.TestCase):
    """TvSeasonWatchProviders200ResponseResultsNO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeasonWatchProviders200ResponseResultsNO:
        """Test TvSeasonWatchProviders200ResponseResultsNO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeasonWatchProviders200ResponseResultsNO`
        """
        model = TvSeasonWatchProviders200ResponseResultsNO()
        if include_optional:
            return TvSeasonWatchProviders200ResponseResultsNO(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/season/1/watch?locale=NO',
                buy = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_no_buy_inner.tv_series_watch_providers_200_response_results_NO_buy_inner(
                        logo_path = '/shq88b09gTBYC4hA7K7MUL8Q4zP.jpg', 
                        provider_id = 68, 
                        provider_name = 'Microsoft Store', 
                        display_priority = 9, )
                    ],
                flatrate = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_ar_flatrate_inner.tv_series_watch_providers_200_response_results_AR_flatrate_inner(
                        logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg', 
                        provider_id = 384, 
                        provider_name = 'HBO Max', 
                        display_priority = 5, )
                    ]
            )
        else:
            return TvSeasonWatchProviders200ResponseResultsNO(
        )
        """

    def testTvSeasonWatchProviders200ResponseResultsNO(self):
        """Test TvSeasonWatchProviders200ResponseResultsNO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
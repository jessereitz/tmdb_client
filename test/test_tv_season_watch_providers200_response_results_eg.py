# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_season_watch_providers200_response_results_eg import TvSeasonWatchProviders200ResponseResultsEG

class TestTvSeasonWatchProviders200ResponseResultsEG(unittest.TestCase):
    """TvSeasonWatchProviders200ResponseResultsEG unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeasonWatchProviders200ResponseResultsEG:
        """Test TvSeasonWatchProviders200ResponseResultsEG
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeasonWatchProviders200ResponseResultsEG`
        """
        model = TvSeasonWatchProviders200ResponseResultsEG()
        if include_optional:
            return TvSeasonWatchProviders200ResponseResultsEG(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/season/1/watch?locale=EG',
                flatrate = [
                    tmdb_client.models.tv_season_watch_providers_200_response_results_eg_flatrate_inner.tv_season_watch_providers_200_response_results_EG_flatrate_inner(
                        logo_path = '/xEPXbwbfABzPrUTWbgtDFH1NOa.jpg', 
                        provider_id = 629, 
                        provider_name = 'OSN', 
                        display_priority = 28, )
                    ]
            )
        else:
            return TvSeasonWatchProviders200ResponseResultsEG(
        )
        """

    def testTvSeasonWatchProviders200ResponseResultsEG(self):
        """Test TvSeasonWatchProviders200ResponseResultsEG"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

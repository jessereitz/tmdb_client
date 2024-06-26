# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_season_watch_providers200_response_results_do import TvSeasonWatchProviders200ResponseResultsDO

class TestTvSeasonWatchProviders200ResponseResultsDO(unittest.TestCase):
    """TvSeasonWatchProviders200ResponseResultsDO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeasonWatchProviders200ResponseResultsDO:
        """Test TvSeasonWatchProviders200ResponseResultsDO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeasonWatchProviders200ResponseResultsDO`
        """
        model = TvSeasonWatchProviders200ResponseResultsDO()
        if include_optional:
            return TvSeasonWatchProviders200ResponseResultsDO(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/season/1/watch?locale=DO',
                flatrate = [
                    tmdb_client.models.movie_watch_providers_200_response_results_bb_flatrate_inner.movie_watch_providers_200_response_results_BB_flatrate_inner(
                        logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg', 
                        provider_id = 384, 
                        provider_name = 'HBO Max', 
                        display_priority = 28, )
                    ]
            )
        else:
            return TvSeasonWatchProviders200ResponseResultsDO(
        )
        """

    def testTvSeasonWatchProviders200ResponseResultsDO(self):
        """Test TvSeasonWatchProviders200ResponseResultsDO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_season_watch_providers200_response_results_jm import TvSeasonWatchProviders200ResponseResultsJM

class TestTvSeasonWatchProviders200ResponseResultsJM(unittest.TestCase):
    """TvSeasonWatchProviders200ResponseResultsJM unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeasonWatchProviders200ResponseResultsJM:
        """Test TvSeasonWatchProviders200ResponseResultsJM
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeasonWatchProviders200ResponseResultsJM`
        """
        model = TvSeasonWatchProviders200ResponseResultsJM()
        if include_optional:
            return TvSeasonWatchProviders200ResponseResultsJM(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/season/1/watch?locale=JM',
                flatrate = [
                    tmdb_client.models.movie_watch_providers_200_response_results_jm_flatrate_inner.movie_watch_providers_200_response_results_JM_flatrate_inner(
                        logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg', 
                        provider_id = 384, 
                        provider_name = 'HBO Max', 
                        display_priority = 27, )
                    ]
            )
        else:
            return TvSeasonWatchProviders200ResponseResultsJM(
        )
        """

    def testTvSeasonWatchProviders200ResponseResultsJM(self):
        """Test TvSeasonWatchProviders200ResponseResultsJM"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

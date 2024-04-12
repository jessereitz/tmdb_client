# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_ug import TvSeriesWatchProviders200ResponseResultsUG

class TestTvSeriesWatchProviders200ResponseResultsUG(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsUG unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsUG:
        """Test TvSeriesWatchProviders200ResponseResultsUG
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsUG`
        """
        model = TvSeriesWatchProviders200ResponseResultsUG()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsUG(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=UG',
                flatrate = [
                    tmdb_client.models.tv_series_watch_providers_200_response_results_ke_flatrate_inner.tv_series_watch_providers_200_response_results_KE_flatrate_inner(
                        logo_path = '/okiQZMXnqwv0aD3QDYmu5DBNLce.jpg', 
                        provider_id = 55, 
                        provider_name = 'ShowMax', 
                        display_priority = 10, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsUG(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsUG(self):
        """Test TvSeriesWatchProviders200ResponseResultsUG"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_ci import TvSeriesWatchProviders200ResponseResultsCI

class TestTvSeriesWatchProviders200ResponseResultsCI(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsCI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsCI:
        """Test TvSeriesWatchProviders200ResponseResultsCI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsCI`
        """
        model = TvSeriesWatchProviders200ResponseResultsCI()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsCI(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=CI',
                flatrate = [
                    tmdb_client.models.tv_series_watch_providers_200_response_results_ci_flatrate_inner.tv_series_watch_providers_200_response_results_CI_flatrate_inner(
                        logo_path = '/okiQZMXnqwv0aD3QDYmu5DBNLce.jpg', 
                        provider_id = 55, 
                        provider_name = 'ShowMax', 
                        display_priority = 25, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsCI(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsCI(self):
        """Test TvSeriesWatchProviders200ResponseResultsCI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

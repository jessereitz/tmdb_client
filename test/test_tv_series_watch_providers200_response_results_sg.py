# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_sg import TvSeriesWatchProviders200ResponseResultsSG

class TestTvSeriesWatchProviders200ResponseResultsSG(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsSG unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsSG:
        """Test TvSeriesWatchProviders200ResponseResultsSG
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsSG`
        """
        model = TvSeriesWatchProviders200ResponseResultsSG()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsSG(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=SG',
                flatrate = [
                    tmdb_client.models.tv_series_watch_providers_200_response_results_sg_flatrate_inner.tv_series_watch_providers_200_response_results_SG_flatrate_inner(
                        logo_path = '/bxdNcDbk1ohVeOMmM3eusAAiTLw.jpg', 
                        provider_id = 425, 
                        provider_name = 'HBO Go', 
                        display_priority = 13, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsSG(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsSG(self):
        """Test TvSeriesWatchProviders200ResponseResultsSG"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

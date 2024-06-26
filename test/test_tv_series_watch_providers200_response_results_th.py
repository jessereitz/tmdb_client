# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_th import TvSeriesWatchProviders200ResponseResultsTH

class TestTvSeriesWatchProviders200ResponseResultsTH(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsTH unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsTH:
        """Test TvSeriesWatchProviders200ResponseResultsTH
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsTH`
        """
        model = TvSeriesWatchProviders200ResponseResultsTH()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsTH(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=TH',
                flatrate = [
                    tmdb_client.models.tv_series_watch_providers_200_response_results_ph_flatrate_inner.tv_series_watch_providers_200_response_results_PH_flatrate_inner(
                        logo_path = '/bxdNcDbk1ohVeOMmM3eusAAiTLw.jpg', 
                        provider_id = 425, 
                        provider_name = 'HBO Go', 
                        display_priority = 12, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsTH(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsTH(self):
        """Test TvSeriesWatchProviders200ResponseResultsTH"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

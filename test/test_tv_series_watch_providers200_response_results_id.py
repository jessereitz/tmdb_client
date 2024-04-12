# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_id import TvSeriesWatchProviders200ResponseResultsID

class TestTvSeriesWatchProviders200ResponseResultsID(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsID unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsID:
        """Test TvSeriesWatchProviders200ResponseResultsID
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsID`
        """
        model = TvSeriesWatchProviders200ResponseResultsID()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsID(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=ID',
                flatrate = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_id_flatrate_inner.tv_series_watch_providers_200_response_results_ID_flatrate_inner(
                        logo_path = '/bxdNcDbk1ohVeOMmM3eusAAiTLw.jpg', 
                        provider_id = 425, 
                        provider_name = 'HBO Go', 
                        display_priority = 14, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsID(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsID(self):
        """Test TvSeriesWatchProviders200ResponseResultsID"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

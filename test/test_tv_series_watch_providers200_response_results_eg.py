# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_eg import TvSeriesWatchProviders200ResponseResultsEG

class TestTvSeriesWatchProviders200ResponseResultsEG(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsEG unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsEG:
        """Test TvSeriesWatchProviders200ResponseResultsEG
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsEG`
        """
        model = TvSeriesWatchProviders200ResponseResultsEG()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsEG(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=EG',
                flatrate = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_eg_flatrate_inner.tv_series_watch_providers_200_response_results_EG_flatrate_inner(
                        logo_path = '/xEPXbwbfABzPrUTWbgtDFH1NOa.jpg', 
                        provider_id = 629, 
                        provider_name = 'OSN', 
                        display_priority = 27, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsEG(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsEG(self):
        """Test TvSeriesWatchProviders200ResponseResultsEG"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

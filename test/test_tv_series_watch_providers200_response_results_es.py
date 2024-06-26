# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_es import TvSeriesWatchProviders200ResponseResultsES

class TestTvSeriesWatchProviders200ResponseResultsES(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsES unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsES:
        """Test TvSeriesWatchProviders200ResponseResultsES
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsES`
        """
        model = TvSeriesWatchProviders200ResponseResultsES()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsES(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=ES',
                flatrate = [
                    tmdb_client.models.tv_series_watch_providers_200_response_results_es_flatrate_inner.tv_series_watch_providers_200_response_results_ES_flatrate_inner(
                        logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg', 
                        provider_id = 384, 
                        provider_name = 'HBO Max', 
                        display_priority = 9, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsES(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsES(self):
        """Test TvSeriesWatchProviders200ResponseResultsES"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

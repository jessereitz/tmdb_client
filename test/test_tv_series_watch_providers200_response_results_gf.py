# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_gf import TvSeriesWatchProviders200ResponseResultsGF

class TestTvSeriesWatchProviders200ResponseResultsGF(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsGF unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsGF:
        """Test TvSeriesWatchProviders200ResponseResultsGF
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsGF`
        """
        model = TvSeriesWatchProviders200ResponseResultsGF()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsGF(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=GF',
                flatrate = [
                    tmdb_client.models.movie_watch_providers_200_response_results_gf_flatrate_inner.movie_watch_providers_200_response_results_GF_flatrate_inner(
                        logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg', 
                        provider_id = 384, 
                        provider_name = 'HBO Max', 
                        display_priority = 30, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsGF(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsGF(self):
        """Test TvSeriesWatchProviders200ResponseResultsGF"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

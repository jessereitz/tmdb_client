# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_bs import TvSeriesWatchProviders200ResponseResultsBS

class TestTvSeriesWatchProviders200ResponseResultsBS(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsBS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsBS:
        """Test TvSeriesWatchProviders200ResponseResultsBS
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsBS`
        """
        model = TvSeriesWatchProviders200ResponseResultsBS()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsBS(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=BS',
                flatrate = [
                    openapi_client.models.movie_watch_providers_200_response_results_bb_flatrate_inner.movie_watch_providers_200_response_results_BB_flatrate_inner(
                        logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg', 
                        provider_id = 384, 
                        provider_name = 'HBO Max', 
                        display_priority = 28, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsBS(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsBS(self):
        """Test TvSeriesWatchProviders200ResponseResultsBS"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
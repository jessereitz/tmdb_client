# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_md import MovieWatchProviders200ResponseResultsMD

class TestMovieWatchProviders200ResponseResultsMD(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsMD unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsMD:
        """Test MovieWatchProviders200ResponseResultsMD
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsMD`
        """
        model = MovieWatchProviders200ResponseResultsMD()
        if include_optional:
            return MovieWatchProviders200ResponseResultsMD(
                link = 'https://www.themoviedb.org/movie/550-fight-club/watch?locale=MD',
                buy = [
                    tmdb_client.models.movie_watch_providers_200_response_results_bh_buy_inner.movie_watch_providers_200_response_results_BH_buy_inner(
                        logo_path = '/tbEdFQDwx5LEVr8WpSeXQSIirVq.jpg', 
                        provider_id = 3, 
                        provider_name = 'Google Play Movies', 
                        display_priority = 1000, )
                    ],
                flatrate = [
                    tmdb_client.models.movie_watch_providers_200_response_results_md_flatrate_inner.movie_watch_providers_200_response_results_MD_flatrate_inner(
                        logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg', 
                        provider_id = 384, 
                        provider_name = 'HBO Max', 
                        display_priority = 26, )
                    ]
            )
        else:
            return MovieWatchProviders200ResponseResultsMD(
        )
        """

    def testMovieWatchProviders200ResponseResultsMD(self):
        """Test MovieWatchProviders200ResponseResultsMD"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

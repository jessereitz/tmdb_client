# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_it import MovieWatchProviders200ResponseResultsIT

class TestMovieWatchProviders200ResponseResultsIT(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsIT unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsIT:
        """Test MovieWatchProviders200ResponseResultsIT
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsIT`
        """
        model = MovieWatchProviders200ResponseResultsIT()
        if include_optional:
            return MovieWatchProviders200ResponseResultsIT(
                link = 'https://www.themoviedb.org/movie/550-fight-club/watch?locale=IT',
                buy = [
                    tmdb_client.models.movie_watch_providers_200_response_results_it_buy_inner.movie_watch_providers_200_response_results_IT_buy_inner(
                        logo_path = '/5GEbAhFW2S5T8zVc1MNvz00pIzM.jpg', 
                        provider_id = 35, 
                        provider_name = 'Rakuten TV', 
                        display_priority = 3, )
                    ],
                rent = [
                    tmdb_client.models.movie_watch_providers_200_response_results_it_buy_inner.movie_watch_providers_200_response_results_IT_buy_inner(
                        logo_path = '/5GEbAhFW2S5T8zVc1MNvz00pIzM.jpg', 
                        provider_id = 35, 
                        provider_name = 'Rakuten TV', 
                        display_priority = 3, )
                    ],
                flatrate = [
                    tmdb_client.models.movie_watch_providers_200_response_results_au_flatrate_inner.movie_watch_providers_200_response_results_AU_flatrate_inner(
                        logo_path = '/emthp39XA2YScoYL1p0sdbAH2WA.jpg', 
                        provider_id = 119, 
                        provider_name = 'Amazon Prime Video', 
                        display_priority = 1, )
                    ]
            )
        else:
            return MovieWatchProviders200ResponseResultsIT(
        )
        """

    def testMovieWatchProviders200ResponseResultsIT(self):
        """Test MovieWatchProviders200ResponseResultsIT"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

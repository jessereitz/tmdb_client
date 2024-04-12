# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_ca import MovieWatchProviders200ResponseResultsCA

class TestMovieWatchProviders200ResponseResultsCA(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsCA unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsCA:
        """Test MovieWatchProviders200ResponseResultsCA
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsCA`
        """
        model = MovieWatchProviders200ResponseResultsCA()
        if include_optional:
            return MovieWatchProviders200ResponseResultsCA(
                link = 'https://www.themoviedb.org/movie/550-fight-club/watch?locale=CA',
                rent = [
                    tmdb_client.models.movie_watch_providers_200_response_results_ca_rent_inner.movie_watch_providers_200_response_results_CA_rent_inner(
                        logo_path = '/tbEdFQDwx5LEVr8WpSeXQSIirVq.jpg', 
                        provider_id = 3, 
                        provider_name = 'Google Play Movies', 
                        display_priority = 8, )
                    ],
                buy = [
                    tmdb_client.models.movie_watch_providers_200_response_results_be_rent_inner.movie_watch_providers_200_response_results_BE_rent_inner(
                        logo_path = '/peURlLlr8jggOwK53fJ5wdQl05y.jpg', 
                        provider_id = 2, 
                        provider_name = 'Apple TV', 
                        display_priority = 6, )
                    ],
                flatrate = [
                    tmdb_client.models.movie_watch_providers_200_response_results_ca_flatrate_inner.movie_watch_providers_200_response_results_CA_flatrate_inner(
                        logo_path = '/sB5vHrmYmliwUvBwZe8HpXo9r8m.jpg', 
                        provider_id = 305, 
                        provider_name = 'Crave Starz', 
                        display_priority = 5, )
                    ]
            )
        else:
            return MovieWatchProviders200ResponseResultsCA(
        )
        """

    def testMovieWatchProviders200ResponseResultsCA(self):
        """Test MovieWatchProviders200ResponseResultsCA"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_uy import MovieWatchProviders200ResponseResultsUY

class TestMovieWatchProviders200ResponseResultsUY(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsUY unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsUY:
        """Test MovieWatchProviders200ResponseResultsUY
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsUY`
        """
        model = MovieWatchProviders200ResponseResultsUY()
        if include_optional:
            return MovieWatchProviders200ResponseResultsUY(
                link = 'https://www.themoviedb.org/movie/550-fight-club/watch?locale=UY',
                flatrate = [
                    tmdb_client.models.movie_watch_providers_200_response_results_au_flatrate_inner.movie_watch_providers_200_response_results_AU_flatrate_inner(
                        logo_path = '/emthp39XA2YScoYL1p0sdbAH2WA.jpg', 
                        provider_id = 119, 
                        provider_name = 'Amazon Prime Video', 
                        display_priority = 1, )
                    ]
            )
        else:
            return MovieWatchProviders200ResponseResultsUY(
        )
        """

    def testMovieWatchProviders200ResponseResultsUY(self):
        """Test MovieWatchProviders200ResponseResultsUY"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_th import MovieWatchProviders200ResponseResultsTH

class TestMovieWatchProviders200ResponseResultsTH(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsTH unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsTH:
        """Test MovieWatchProviders200ResponseResultsTH
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsTH`
        """
        model = MovieWatchProviders200ResponseResultsTH()
        if include_optional:
            return MovieWatchProviders200ResponseResultsTH(
                link = 'https://www.themoviedb.org/movie/550-fight-club/watch?locale=TH',
                flatrate = [
                    tmdb_client.models.movie_watch_providers_200_response_results_my_flatrate_inner.movie_watch_providers_200_response_results_MY_flatrate_inner(
                        logo_path = '/7Fl8ylPDclt3ZYgNbW2t7rbZE9I.jpg', 
                        provider_id = 122, 
                        provider_name = 'Hotstar', 
                        display_priority = 0, )
                    ]
            )
        else:
            return MovieWatchProviders200ResponseResultsTH(
        )
        """

    def testMovieWatchProviders200ResponseResultsTH(self):
        """Test MovieWatchProviders200ResponseResultsTH"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

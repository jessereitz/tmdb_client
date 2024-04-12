# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_watch_providers200_response_results_id import MovieWatchProviders200ResponseResultsID

class TestMovieWatchProviders200ResponseResultsID(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsID unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsID:
        """Test MovieWatchProviders200ResponseResultsID
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsID`
        """
        model = MovieWatchProviders200ResponseResultsID()
        if include_optional:
            return MovieWatchProviders200ResponseResultsID(
                link = 'https://www.themoviedb.org/movie/550-fight-club/watch?locale=ID',
                flatrate = [
                    openapi_client.models.movie_watch_providers_200_response_results_id_flatrate_inner.movie_watch_providers_200_response_results_ID_flatrate_inner(
                        logo_path = '/7Fl8ylPDclt3ZYgNbW2t7rbZE9I.jpg', 
                        provider_id = 122, 
                        provider_name = 'Hotstar', 
                        display_priority = 3, )
                    ]
            )
        else:
            return MovieWatchProviders200ResponseResultsID(
        )
        """

    def testMovieWatchProviders200ResponseResultsID(self):
        """Test MovieWatchProviders200ResponseResultsID"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_watch_providers200_response_results_sm import MovieWatchProviders200ResponseResultsSM

class TestMovieWatchProviders200ResponseResultsSM(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsSM unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsSM:
        """Test MovieWatchProviders200ResponseResultsSM
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsSM`
        """
        model = MovieWatchProviders200ResponseResultsSM()
        if include_optional:
            return MovieWatchProviders200ResponseResultsSM(
                link = 'https://www.themoviedb.org/movie/550-fight-club/watch?locale=SM',
                flatrate = [
                    openapi_client.models.movie_watch_providers_200_response_results_li_flatrate_inner.movie_watch_providers_200_response_results_LI_flatrate_inner(
                        logo_path = '/7rwgEs15tFwyR9NPQ5vpzxTj19Q.jpg', 
                        provider_id = 337, 
                        provider_name = 'Disney Plus', 
                        display_priority = 30, )
                    ]
            )
        else:
            return MovieWatchProviders200ResponseResultsSM(
        )
        """

    def testMovieWatchProviders200ResponseResultsSM(self):
        """Test MovieWatchProviders200ResponseResultsSM"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
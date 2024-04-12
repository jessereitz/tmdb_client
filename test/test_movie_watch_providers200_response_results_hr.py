# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_watch_providers200_response_results_hr import MovieWatchProviders200ResponseResultsHR

class TestMovieWatchProviders200ResponseResultsHR(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsHR unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsHR:
        """Test MovieWatchProviders200ResponseResultsHR
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsHR`
        """
        model = MovieWatchProviders200ResponseResultsHR()
        if include_optional:
            return MovieWatchProviders200ResponseResultsHR(
                link = 'https://www.themoviedb.org/movie/550-fight-club/watch?locale=HR',
                buy = [
                    openapi_client.models.movie_watch_providers_200_response_results_co_buy_inner.movie_watch_providers_200_response_results_CO_buy_inner(
                        logo_path = '/tbEdFQDwx5LEVr8WpSeXQSIirVq.jpg', 
                        provider_id = 3, 
                        provider_name = 'Google Play Movies', 
                        display_priority = 3, )
                    ],
                ads = [
                    openapi_client.models.movie_watch_providers_200_response_results_hr_ads_inner.movie_watch_providers_200_response_results_HR_ads_inner(
                        logo_path = '/xrHrIraInfRXnrz1zHhY1tXJowg.jpg', 
                        provider_id = 572, 
                        provider_name = 'RTL Play', 
                        display_priority = 30, )
                    ],
                flatrate = [
                    openapi_client.models.movie_watch_providers_200_response_results_au_flatrate_inner.movie_watch_providers_200_response_results_AU_flatrate_inner(
                        logo_path = '/emthp39XA2YScoYL1p0sdbAH2WA.jpg', 
                        provider_id = 119, 
                        provider_name = 'Amazon Prime Video', 
                        display_priority = 1, )
                    ]
            )
        else:
            return MovieWatchProviders200ResponseResultsHR(
        )
        """

    def testMovieWatchProviders200ResponseResultsHR(self):
        """Test MovieWatchProviders200ResponseResultsHR"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

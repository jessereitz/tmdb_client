# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_ru_rent_inner import MovieWatchProviders200ResponseResultsRURentInner

class TestMovieWatchProviders200ResponseResultsRURentInner(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsRURentInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsRURentInner:
        """Test MovieWatchProviders200ResponseResultsRURentInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsRURentInner`
        """
        model = MovieWatchProviders200ResponseResultsRURentInner()
        if include_optional:
            return MovieWatchProviders200ResponseResultsRURentInner(
                logo_path = '/o9ExgOSLF3OTwR6T3DJOuwOKJgq.jpg',
                provider_id = 113,
                provider_name = 'Ivi',
                display_priority = 1000
            )
        else:
            return MovieWatchProviders200ResponseResultsRURentInner(
        )
        """

    def testMovieWatchProviders200ResponseResultsRURentInner(self):
        """Test MovieWatchProviders200ResponseResultsRURentInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

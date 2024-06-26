# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_ca_flatrate_inner import MovieWatchProviders200ResponseResultsCAFlatrateInner

class TestMovieWatchProviders200ResponseResultsCAFlatrateInner(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsCAFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsCAFlatrateInner:
        """Test MovieWatchProviders200ResponseResultsCAFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsCAFlatrateInner`
        """
        model = MovieWatchProviders200ResponseResultsCAFlatrateInner()
        if include_optional:
            return MovieWatchProviders200ResponseResultsCAFlatrateInner(
                logo_path = '/sB5vHrmYmliwUvBwZe8HpXo9r8m.jpg',
                provider_id = 305,
                provider_name = 'Crave Starz',
                display_priority = 5
            )
        else:
            return MovieWatchProviders200ResponseResultsCAFlatrateInner(
        )
        """

    def testMovieWatchProviders200ResponseResultsCAFlatrateInner(self):
        """Test MovieWatchProviders200ResponseResultsCAFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

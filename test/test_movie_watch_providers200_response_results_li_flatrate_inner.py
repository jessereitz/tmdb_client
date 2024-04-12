# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_li_flatrate_inner import MovieWatchProviders200ResponseResultsLIFlatrateInner

class TestMovieWatchProviders200ResponseResultsLIFlatrateInner(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsLIFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsLIFlatrateInner:
        """Test MovieWatchProviders200ResponseResultsLIFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsLIFlatrateInner`
        """
        model = MovieWatchProviders200ResponseResultsLIFlatrateInner()
        if include_optional:
            return MovieWatchProviders200ResponseResultsLIFlatrateInner(
                logo_path = '/7rwgEs15tFwyR9NPQ5vpzxTj19Q.jpg',
                provider_id = 337,
                provider_name = 'Disney Plus',
                display_priority = 30
            )
        else:
            return MovieWatchProviders200ResponseResultsLIFlatrateInner(
        )
        """

    def testMovieWatchProviders200ResponseResultsLIFlatrateInner(self):
        """Test MovieWatchProviders200ResponseResultsLIFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

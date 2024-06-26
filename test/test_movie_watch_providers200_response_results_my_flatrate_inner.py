# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_my_flatrate_inner import MovieWatchProviders200ResponseResultsMYFlatrateInner

class TestMovieWatchProviders200ResponseResultsMYFlatrateInner(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsMYFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsMYFlatrateInner:
        """Test MovieWatchProviders200ResponseResultsMYFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsMYFlatrateInner`
        """
        model = MovieWatchProviders200ResponseResultsMYFlatrateInner()
        if include_optional:
            return MovieWatchProviders200ResponseResultsMYFlatrateInner(
                logo_path = '/7Fl8ylPDclt3ZYgNbW2t7rbZE9I.jpg',
                provider_id = 122,
                provider_name = 'Hotstar',
                display_priority = 0
            )
        else:
            return MovieWatchProviders200ResponseResultsMYFlatrateInner(
        )
        """

    def testMovieWatchProviders200ResponseResultsMYFlatrateInner(self):
        """Test MovieWatchProviders200ResponseResultsMYFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_mk_flatrate_inner import MovieWatchProviders200ResponseResultsMKFlatrateInner

class TestMovieWatchProviders200ResponseResultsMKFlatrateInner(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsMKFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsMKFlatrateInner:
        """Test MovieWatchProviders200ResponseResultsMKFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsMKFlatrateInner`
        """
        model = MovieWatchProviders200ResponseResultsMKFlatrateInner()
        if include_optional:
            return MovieWatchProviders200ResponseResultsMKFlatrateInner(
                logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg',
                provider_id = 384,
                provider_name = 'HBO Max',
                display_priority = 29
            )
        else:
            return MovieWatchProviders200ResponseResultsMKFlatrateInner(
        )
        """

    def testMovieWatchProviders200ResponseResultsMKFlatrateInner(self):
        """Test MovieWatchProviders200ResponseResultsMKFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

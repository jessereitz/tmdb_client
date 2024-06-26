# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_bb_flatrate_inner import MovieWatchProviders200ResponseResultsBBFlatrateInner

class TestMovieWatchProviders200ResponseResultsBBFlatrateInner(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsBBFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsBBFlatrateInner:
        """Test MovieWatchProviders200ResponseResultsBBFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsBBFlatrateInner`
        """
        model = MovieWatchProviders200ResponseResultsBBFlatrateInner()
        if include_optional:
            return MovieWatchProviders200ResponseResultsBBFlatrateInner(
                logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg',
                provider_id = 384,
                provider_name = 'HBO Max',
                display_priority = 28
            )
        else:
            return MovieWatchProviders200ResponseResultsBBFlatrateInner(
        )
        """

    def testMovieWatchProviders200ResponseResultsBBFlatrateInner(self):
        """Test MovieWatchProviders200ResponseResultsBBFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.trending_tv200_response_results_inner import TrendingTv200ResponseResultsInner

class TestTrendingTv200ResponseResultsInner(unittest.TestCase):
    """TrendingTv200ResponseResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrendingTv200ResponseResultsInner:
        """Test TrendingTv200ResponseResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrendingTv200ResponseResultsInner`
        """
        model = TrendingTv200ResponseResultsInner()
        if include_optional:
            return TrendingTv200ResponseResultsInner(
                adult = False,
                backdrop_path = '/8P15FsYcTwQZ4G5rRMd1TKD14Aq.jpg',
                id = 103768,
                name = 'Sweet Tooth',
                original_language = 'en',
                original_name = 'Sweet Tooth',
                overview = 'On a perilous adventure across a post-apocalyptic world, a lovable boy who's half-human and half-deer searches for a new beginning with a gruff protector.',
                poster_path = '/dBxxtfhC4vYrxB2fLsSxOTY2dQc.jpg',
                media_type = 'tv',
                genre_ids = [
                    18
                    ],
                popularity = 137.498,
                first_air_date = '2021-06-04',
                vote_average = 7.928,
                vote_count = 1094,
                origin_country = [
                    'US'
                    ]
            )
        else:
            return TrendingTv200ResponseResultsInner(
        )
        """

    def testTrendingTv200ResponseResultsInner(self):
        """Test TrendingTv200ResponseResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

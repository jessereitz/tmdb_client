# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.account_watchlist_tv200_response_results_inner import AccountWatchlistTv200ResponseResultsInner

class TestAccountWatchlistTv200ResponseResultsInner(unittest.TestCase):
    """AccountWatchlistTv200ResponseResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountWatchlistTv200ResponseResultsInner:
        """Test AccountWatchlistTv200ResponseResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountWatchlistTv200ResponseResultsInner`
        """
        model = AccountWatchlistTv200ResponseResultsInner()
        if include_optional:
            return AccountWatchlistTv200ResponseResultsInner(
                adult = False,
                backdrop_path = '/7phlGHRupo38EnuwmkAHdNUqov3.jpg',
                genre_ids = [
                    35
                    ],
                id = 58932,
                origin_country = [
                    'US'
                    ],
                original_language = 'en',
                original_name = 'The Crazy Ones',
                overview = 'The Crazy Ones is an American situation comedy series created by David E. Kelley that stars Robin Williams and Sarah Michelle Gellar. The single-camera project premiered on CBS on September 26, 2013, as part of the 2013–14 American television season as a Thursday night 9 pm entry. Bill D'Elia, Dean Lorey, Jason Winer, John Montgomery and Mark Teitelbaum serve as executive producers for 20th Century Fox Television.',
                popularity = 8.939,
                poster_path = '/s2e7hTrdmNUaJDf0yDP5b4AHvrD.jpg',
                first_air_date = '2013-09-26',
                name = 'The Crazy Ones',
                vote_average = 6.176,
                vote_count = 94
            )
        else:
            return AccountWatchlistTv200ResponseResultsInner(
        )
        """

    def testAccountWatchlistTv200ResponseResultsInner(self):
        """Test AccountWatchlistTv200ResponseResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

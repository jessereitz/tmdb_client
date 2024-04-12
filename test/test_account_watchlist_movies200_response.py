# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.account_watchlist_movies200_response import AccountWatchlistMovies200Response

class TestAccountWatchlistMovies200Response(unittest.TestCase):
    """AccountWatchlistMovies200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountWatchlistMovies200Response:
        """Test AccountWatchlistMovies200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountWatchlistMovies200Response`
        """
        model = AccountWatchlistMovies200Response()
        if include_optional:
            return AccountWatchlistMovies200Response(
                page = 1,
                results = [
                    openapi_client.models.account_watchlist_movies_200_response_results_inner.account_watchlist_movies_200_response_results_inner(
                        adult = False, 
                        backdrop_path = '/rgNzvSagnlc32TuMEBa529QFIig.jpg', 
                        genre_ids = [
                            878
                            ], 
                        id = 76726, 
                        original_language = 'en', 
                        original_title = 'Chronicle', 
                        overview = 'Three high school students make an incredible discovery, leading to their developing uncanny powers beyond their understanding. As they learn to control their abilities and use them to their advantage, their lives start to spin out of control, and their darker sides begin to take over.', 
                        popularity = 37.148, 
                        poster_path = '/xENglsVIIWEEhhB5lgpy33tGcKI.jpg', 
                        release_date = '2012-02-01', 
                        title = 'Chronicle', 
                        video = False, 
                        vote_average = 6.822, 
                        vote_count = 4741, )
                    ],
                total_pages = 34,
                total_results = 677
            )
        else:
            return AccountWatchlistMovies200Response(
        )
        """

    def testAccountWatchlistMovies200Response(self):
        """Test AccountWatchlistMovies200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
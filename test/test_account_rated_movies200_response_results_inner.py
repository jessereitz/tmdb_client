# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.account_rated_movies200_response_results_inner import AccountRatedMovies200ResponseResultsInner

class TestAccountRatedMovies200ResponseResultsInner(unittest.TestCase):
    """AccountRatedMovies200ResponseResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountRatedMovies200ResponseResultsInner:
        """Test AccountRatedMovies200ResponseResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountRatedMovies200ResponseResultsInner`
        """
        model = AccountRatedMovies200ResponseResultsInner()
        if include_optional:
            return AccountRatedMovies200ResponseResultsInner(
                adult = False,
                backdrop_path = '/dUVbWINfRMGojGZRcO6GF1Z2nV8.jpg',
                genre_ids = [
                    12
                    ],
                id = 120,
                original_language = 'en',
                original_title = 'The Lord of the Rings: The Fellowship of the Ring',
                overview = 'Young hobbit Frodo Baggins, after inheriting a mysterious ring from his uncle Bilbo, must leave his home in order to keep it from falling into the hands of its evil creator. Along the way, a fellowship is formed to protect the ringbearer and make sure that the ring arrives at its final destination: Mt. Doom, the only place where it can be destroyed.',
                popularity = 84.737,
                poster_path = '/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg',
                release_date = '2001-12-18',
                title = 'The Lord of the Rings: The Fellowship of the Ring',
                video = False,
                vote_average = 8.396,
                vote_count = 22579,
                rating = 8
            )
        else:
            return AccountRatedMovies200ResponseResultsInner(
        )
        """

    def testAccountRatedMovies200ResponseResultsInner(self):
        """Test AccountRatedMovies200ResponseResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
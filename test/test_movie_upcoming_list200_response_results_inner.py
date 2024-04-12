# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_upcoming_list200_response_results_inner import MovieUpcomingList200ResponseResultsInner

class TestMovieUpcomingList200ResponseResultsInner(unittest.TestCase):
    """MovieUpcomingList200ResponseResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieUpcomingList200ResponseResultsInner:
        """Test MovieUpcomingList200ResponseResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieUpcomingList200ResponseResultsInner`
        """
        model = MovieUpcomingList200ResponseResultsInner()
        if include_optional:
            return MovieUpcomingList200ResponseResultsInner(
                adult = False,
                backdrop_path = '/7bWxAsNPv9CXHOhZbJVlj2KxgfP.jpg',
                genre_ids = [
                    27
                    ],
                id = 713704,
                original_language = 'en',
                original_title = 'Evil Dead Rise',
                overview = 'Two sisters find an ancient vinyl that gives birth to bloodthirsty demons that run amok in a Los Angeles apartment building and thrusts them into a primal battle for survival as they face the most nightmarish version of family imaginable.',
                popularity = 1696.367,
                poster_path = '/mIBCtPvKZQlxubxKMeViO2UrP3q.jpg',
                release_date = '2023-04-12',
                title = 'Evil Dead Rise',
                video = False,
                vote_average = 7,
                vote_count = 207
            )
        else:
            return MovieUpcomingList200ResponseResultsInner(
        )
        """

    def testMovieUpcomingList200ResponseResultsInner(self):
        """Test MovieUpcomingList200ResponseResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
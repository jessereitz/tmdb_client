# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_upcoming_list200_response import MovieUpcomingList200Response

class TestMovieUpcomingList200Response(unittest.TestCase):
    """MovieUpcomingList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieUpcomingList200Response:
        """Test MovieUpcomingList200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieUpcomingList200Response`
        """
        model = MovieUpcomingList200Response()
        if include_optional:
            return MovieUpcomingList200Response(
                dates = openapi_client.models.movie_upcoming_list_200_response_dates.movie_upcoming_list_200_response_dates(
                    maximum = '2023-05-23', 
                    minimum = '2023-05-04', ),
                page = 1,
                results = [
                    openapi_client.models.movie_upcoming_list_200_response_results_inner.movie_upcoming_list_200_response_results_inner(
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
                        vote_count = 207, )
                    ],
                total_pages = 19,
                total_results = 369
            )
        else:
            return MovieUpcomingList200Response(
        )
        """

    def testMovieUpcomingList200Response(self):
        """Test MovieUpcomingList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
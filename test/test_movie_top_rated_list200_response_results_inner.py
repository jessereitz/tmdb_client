# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_top_rated_list200_response_results_inner import MovieTopRatedList200ResponseResultsInner

class TestMovieTopRatedList200ResponseResultsInner(unittest.TestCase):
    """MovieTopRatedList200ResponseResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieTopRatedList200ResponseResultsInner:
        """Test MovieTopRatedList200ResponseResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieTopRatedList200ResponseResultsInner`
        """
        model = MovieTopRatedList200ResponseResultsInner()
        if include_optional:
            return MovieTopRatedList200ResponseResultsInner(
                adult = False,
                backdrop_path = '/tmU7GeKVybMWFButWEGl2M4GeiP.jpg',
                genre_ids = [
                    18
                    ],
                id = 238,
                original_language = 'en',
                original_title = 'The Godfather',
                overview = 'Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family. When organized crime family patriarch, Vito Corleone barely survives an attempt on his life, his youngest son, Michael steps in to take care of the would-be killers, launching a campaign of bloody revenge.',
                popularity = 100.932,
                poster_path = '/3bhkrj58Vtu7enYsRolD1fZdja1.jpg',
                release_date = '1972-03-14',
                title = 'The Godfather',
                video = False,
                vote_average = 8.7,
                vote_count = 17806
            )
        else:
            return MovieTopRatedList200ResponseResultsInner(
        )
        """

    def testMovieTopRatedList200ResponseResultsInner(self):
        """Test MovieTopRatedList200ResponseResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

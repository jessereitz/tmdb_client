# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.genre_movie_list200_response_genres_inner import GenreMovieList200ResponseGenresInner

class TestGenreMovieList200ResponseGenresInner(unittest.TestCase):
    """GenreMovieList200ResponseGenresInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenreMovieList200ResponseGenresInner:
        """Test GenreMovieList200ResponseGenresInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenreMovieList200ResponseGenresInner`
        """
        model = GenreMovieList200ResponseGenresInner()
        if include_optional:
            return GenreMovieList200ResponseGenresInner(
                id = 28,
                name = 'Action'
            )
        else:
            return GenreMovieList200ResponseGenresInner(
        )
        """

    def testGenreMovieList200ResponseGenresInner(self):
        """Test GenreMovieList200ResponseGenresInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

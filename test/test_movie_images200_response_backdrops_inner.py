# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_images200_response_backdrops_inner import MovieImages200ResponseBackdropsInner

class TestMovieImages200ResponseBackdropsInner(unittest.TestCase):
    """MovieImages200ResponseBackdropsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieImages200ResponseBackdropsInner:
        """Test MovieImages200ResponseBackdropsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieImages200ResponseBackdropsInner`
        """
        model = MovieImages200ResponseBackdropsInner()
        if include_optional:
            return MovieImages200ResponseBackdropsInner(
                aspect_ratio = 1.778,
                height = 800,
                iso_639_1 = None,
                file_path = '/hZkgoQYus5vegHoetLkCJzb17zJ.jpg',
                vote_average = 5.622,
                vote_count = 20,
                width = 1422
            )
        else:
            return MovieImages200ResponseBackdropsInner(
        )
        """

    def testMovieImages200ResponseBackdropsInner(self):
        """Test MovieImages200ResponseBackdropsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

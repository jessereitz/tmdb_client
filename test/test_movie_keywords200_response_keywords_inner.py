# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_keywords200_response_keywords_inner import MovieKeywords200ResponseKeywordsInner

class TestMovieKeywords200ResponseKeywordsInner(unittest.TestCase):
    """MovieKeywords200ResponseKeywordsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieKeywords200ResponseKeywordsInner:
        """Test MovieKeywords200ResponseKeywordsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieKeywords200ResponseKeywordsInner`
        """
        model = MovieKeywords200ResponseKeywordsInner()
        if include_optional:
            return MovieKeywords200ResponseKeywordsInner(
                id = 818,
                name = 'based on novel or book'
            )
        else:
            return MovieKeywords200ResponseKeywordsInner(
        )
        """

    def testMovieKeywords200ResponseKeywordsInner(self):
        """Test MovieKeywords200ResponseKeywordsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

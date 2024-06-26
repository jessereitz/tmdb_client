# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.search_keyword200_response import SearchKeyword200Response

class TestSearchKeyword200Response(unittest.TestCase):
    """SearchKeyword200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchKeyword200Response:
        """Test SearchKeyword200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchKeyword200Response`
        """
        model = SearchKeyword200Response()
        if include_optional:
            return SearchKeyword200Response(
                page = 1,
                results = [
                    tmdb_client.models.search_keyword_200_response_results_inner.search_keyword_200_response_results_inner(
                        id = 262419, 
                        name = 'lost', )
                    ],
                total_pages = 5,
                total_results = 84
            )
        else:
            return SearchKeyword200Response(
        )
        """

    def testSearchKeyword200Response(self):
        """Test SearchKeyword200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

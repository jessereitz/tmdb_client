# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.search_keyword200_response_results_inner import SearchKeyword200ResponseResultsInner

class TestSearchKeyword200ResponseResultsInner(unittest.TestCase):
    """SearchKeyword200ResponseResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchKeyword200ResponseResultsInner:
        """Test SearchKeyword200ResponseResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchKeyword200ResponseResultsInner`
        """
        model = SearchKeyword200ResponseResultsInner()
        if include_optional:
            return SearchKeyword200ResponseResultsInner(
                id = 262419,
                name = 'lost'
            )
        else:
            return SearchKeyword200ResponseResultsInner(
        )
        """

    def testSearchKeyword200ResponseResultsInner(self):
        """Test SearchKeyword200ResponseResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

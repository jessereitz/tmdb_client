# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.lists_copy200_response_results_inner import ListsCopy200ResponseResultsInner

class TestListsCopy200ResponseResultsInner(unittest.TestCase):
    """ListsCopy200ResponseResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListsCopy200ResponseResultsInner:
        """Test ListsCopy200ResponseResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListsCopy200ResponseResultsInner`
        """
        model = ListsCopy200ResponseResultsInner()
        if include_optional:
            return ListsCopy200ResponseResultsInner(
                description = '',
                favorite_count = 0,
                id = 8257231,
                item_count = 182,
                iso_639_1 = 'en',
                iso_3166_1 = 'US',
                name = 'Done',
                poster_path = None
            )
        else:
            return ListsCopy200ResponseResultsInner(
        )
        """

    def testListsCopy200ResponseResultsInner(self):
        """Test ListsCopy200ResponseResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
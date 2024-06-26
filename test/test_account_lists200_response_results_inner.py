# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.account_lists200_response_results_inner import AccountLists200ResponseResultsInner

class TestAccountLists200ResponseResultsInner(unittest.TestCase):
    """AccountLists200ResponseResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountLists200ResponseResultsInner:
        """Test AccountLists200ResponseResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountLists200ResponseResultsInner`
        """
        model = AccountLists200ResponseResultsInner()
        if include_optional:
            return AccountLists200ResponseResultsInner(
                description = '',
                favorite_count = 0,
                id = 120174,
                item_count = 5,
                iso_639_1 = 'en',
                list_type = 'movie',
                name = 'Test Alpha Sort',
                poster_path = None
            )
        else:
            return AccountLists200ResponseResultsInner(
        )
        """

    def testAccountLists200ResponseResultsInner(self):
        """Test AccountLists200ResponseResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

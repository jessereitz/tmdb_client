# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.account_lists200_response import AccountLists200Response

class TestAccountLists200Response(unittest.TestCase):
    """AccountLists200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountLists200Response:
        """Test AccountLists200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountLists200Response`
        """
        model = AccountLists200Response()
        if include_optional:
            return AccountLists200Response(
                page = 1,
                results = [
                    tmdb_client.models.account_lists_200_response_results_inner.account_lists_200_response_results_inner(
                        description = '', 
                        favorite_count = 0, 
                        id = 120174, 
                        item_count = 5, 
                        iso_639_1 = 'en', 
                        list_type = 'movie', 
                        name = 'Test Alpha Sort', 
                        poster_path = null, )
                    ],
                total_pages = 2,
                total_results = 25
            )
        else:
            return AccountLists200Response(
        )
        """

    def testAccountLists200Response(self):
        """Test AccountLists200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

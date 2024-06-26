# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.lists_copy200_response import ListsCopy200Response

class TestListsCopy200Response(unittest.TestCase):
    """ListsCopy200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListsCopy200Response:
        """Test ListsCopy200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListsCopy200Response`
        """
        model = ListsCopy200Response()
        if include_optional:
            return ListsCopy200Response(
                id = 1399,
                page = 1,
                results = [
                    tmdb_client.models.lists_copy_200_response_results_inner.lists_copy_200_response_results_inner(
                        description = '', 
                        favorite_count = 0, 
                        id = 8257231, 
                        item_count = 182, 
                        iso_639_1 = 'en', 
                        iso_3166_1 = 'US', 
                        name = 'Done', 
                        poster_path = null, )
                    ],
                total_pages = 96,
                total_results = 1906
            )
        else:
            return ListsCopy200Response(
        )
        """

    def testListsCopy200Response(self):
        """Test ListsCopy200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

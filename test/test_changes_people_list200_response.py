# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.changes_people_list200_response import ChangesPeopleList200Response

class TestChangesPeopleList200Response(unittest.TestCase):
    """ChangesPeopleList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChangesPeopleList200Response:
        """Test ChangesPeopleList200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChangesPeopleList200Response`
        """
        model = ChangesPeopleList200Response()
        if include_optional:
            return ChangesPeopleList200Response(
                results = [
                    tmdb_client.models.changes_people_list_200_response_results_inner.changes_people_list_200_response_results_inner(
                        id = 4037513, 
                        adult = False, )
                    ],
                page = 1,
                total_pages = 53,
                total_results = 5292
            )
        else:
            return ChangesPeopleList200Response(
        )
        """

    def testChangesPeopleList200Response(self):
        """Test ChangesPeopleList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

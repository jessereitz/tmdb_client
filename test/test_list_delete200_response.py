# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.list_delete200_response import ListDelete200Response

class TestListDelete200Response(unittest.TestCase):
    """ListDelete200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListDelete200Response:
        """Test ListDelete200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListDelete200Response`
        """
        model = ListDelete200Response()
        if include_optional:
            return ListDelete200Response(
                status_code = 12,
                status_message = 'The item/record was updated successfully.'
            )
        else:
            return ListDelete200Response(
        )
        """

    def testListDelete200Response(self):
        """Test ListDelete200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

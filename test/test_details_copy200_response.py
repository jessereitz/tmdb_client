# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.details_copy200_response import DetailsCopy200Response

class TestDetailsCopy200Response(unittest.TestCase):
    """DetailsCopy200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DetailsCopy200Response:
        """Test DetailsCopy200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DetailsCopy200Response`
        """
        model = DetailsCopy200Response()
        if include_optional:
            return DetailsCopy200Response(
                id = 49,
                results = [
                    openapi_client.models.details_copy_200_response_results_inner.details_copy_200_response_results_inner(
                        name = 'Home Box Office', 
                        type = '', )
                    ]
            )
        else:
            return DetailsCopy200Response(
        )
        """

    def testDetailsCopy200Response(self):
        """Test DetailsCopy200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
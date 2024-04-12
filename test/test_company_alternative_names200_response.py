# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.company_alternative_names200_response import CompanyAlternativeNames200Response

class TestCompanyAlternativeNames200Response(unittest.TestCase):
    """CompanyAlternativeNames200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompanyAlternativeNames200Response:
        """Test CompanyAlternativeNames200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompanyAlternativeNames200Response`
        """
        model = CompanyAlternativeNames200Response()
        if include_optional:
            return CompanyAlternativeNames200Response(
                id = 1,
                results = [
                    openapi_client.models.company_alternative_names_200_response_results_inner.company_alternative_names_200_response_results_inner(
                        name = '루카스필름', 
                        type = '', )
                    ]
            )
        else:
            return CompanyAlternativeNames200Response(
        )
        """

    def testCompanyAlternativeNames200Response(self):
        """Test CompanyAlternativeNames200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

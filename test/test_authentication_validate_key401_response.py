# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.authentication_validate_key401_response import AuthenticationValidateKey401Response

class TestAuthenticationValidateKey401Response(unittest.TestCase):
    """AuthenticationValidateKey401Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthenticationValidateKey401Response:
        """Test AuthenticationValidateKey401Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthenticationValidateKey401Response`
        """
        model = AuthenticationValidateKey401Response()
        if include_optional:
            return AuthenticationValidateKey401Response(
                status_code = 7,
                status_message = 'Invalid API key: You must be granted a valid key.',
                success = False
            )
        else:
            return AuthenticationValidateKey401Response(
        )
        """

    def testAuthenticationValidateKey401Response(self):
        """Test AuthenticationValidateKey401Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

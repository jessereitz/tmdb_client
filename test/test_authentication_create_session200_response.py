# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.authentication_create_session200_response import AuthenticationCreateSession200Response

class TestAuthenticationCreateSession200Response(unittest.TestCase):
    """AuthenticationCreateSession200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthenticationCreateSession200Response:
        """Test AuthenticationCreateSession200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthenticationCreateSession200Response`
        """
        model = AuthenticationCreateSession200Response()
        if include_optional:
            return AuthenticationCreateSession200Response(
                success = True,
                session_id = '79191836ddaa0da3df76a5ffef6f07ad6ab0c641'
            )
        else:
            return AuthenticationCreateSession200Response(
        )
        """

    def testAuthenticationCreateSession200Response(self):
        """Test AuthenticationCreateSession200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

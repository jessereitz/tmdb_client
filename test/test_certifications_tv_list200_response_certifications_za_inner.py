# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.certifications_tv_list200_response_certifications_za_inner import CertificationsTvList200ResponseCertificationsZAInner

class TestCertificationsTvList200ResponseCertificationsZAInner(unittest.TestCase):
    """CertificationsTvList200ResponseCertificationsZAInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationsTvList200ResponseCertificationsZAInner:
        """Test CertificationsTvList200ResponseCertificationsZAInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationsTvList200ResponseCertificationsZAInner`
        """
        model = CertificationsTvList200ResponseCertificationsZAInner()
        if include_optional:
            return CertificationsTvList200ResponseCertificationsZAInner(
                certification = 'All',
                meaning = 'This is a programme/film that does not contain any obscenity, and is suitable for family viewing. A logo must be displayed in the corner of the screen for 30 seconds after each commercial break.',
                order = 1
            )
        else:
            return CertificationsTvList200ResponseCertificationsZAInner(
        )
        """

    def testCertificationsTvList200ResponseCertificationsZAInner(self):
        """Test CertificationsTvList200ResponseCertificationsZAInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.certifications_tv_list200_response_certifications_ca_inner import CertificationsTvList200ResponseCertificationsCAInner

class TestCertificationsTvList200ResponseCertificationsCAInner(unittest.TestCase):
    """CertificationsTvList200ResponseCertificationsCAInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationsTvList200ResponseCertificationsCAInner:
        """Test CertificationsTvList200ResponseCertificationsCAInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationsTvList200ResponseCertificationsCAInner`
        """
        model = CertificationsTvList200ResponseCertificationsCAInner()
        if include_optional:
            return CertificationsTvList200ResponseCertificationsCAInner(
                certification = 'Exempt',
                meaning = 'Shows which are exempt from ratings (such as news and sports programming) will not display an on-screen rating at all.',
                order = 1
            )
        else:
            return CertificationsTvList200ResponseCertificationsCAInner(
        )
        """

    def testCertificationsTvList200ResponseCertificationsCAInner(self):
        """Test CertificationsTvList200ResponseCertificationsCAInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

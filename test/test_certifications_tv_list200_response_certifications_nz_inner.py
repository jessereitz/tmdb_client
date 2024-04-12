# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.certifications_tv_list200_response_certifications_nz_inner import CertificationsTvList200ResponseCertificationsNZInner

class TestCertificationsTvList200ResponseCertificationsNZInner(unittest.TestCase):
    """CertificationsTvList200ResponseCertificationsNZInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationsTvList200ResponseCertificationsNZInner:
        """Test CertificationsTvList200ResponseCertificationsNZInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationsTvList200ResponseCertificationsNZInner`
        """
        model = CertificationsTvList200ResponseCertificationsNZInner()
        if include_optional:
            return CertificationsTvList200ResponseCertificationsNZInner(
                certification = 'G',
                meaning = 'Approved for general viewing.',
                order = 1
            )
        else:
            return CertificationsTvList200ResponseCertificationsNZInner(
        )
        """

    def testCertificationsTvList200ResponseCertificationsNZInner(self):
        """Test CertificationsTvList200ResponseCertificationsNZInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

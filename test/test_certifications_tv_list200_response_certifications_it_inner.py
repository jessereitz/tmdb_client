# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.certifications_tv_list200_response_certifications_it_inner import CertificationsTvList200ResponseCertificationsITInner

class TestCertificationsTvList200ResponseCertificationsITInner(unittest.TestCase):
    """CertificationsTvList200ResponseCertificationsITInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationsTvList200ResponseCertificationsITInner:
        """Test CertificationsTvList200ResponseCertificationsITInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationsTvList200ResponseCertificationsITInner`
        """
        model = CertificationsTvList200ResponseCertificationsITInner()
        if include_optional:
            return CertificationsTvList200ResponseCertificationsITInner(
                certification = 'T',
                meaning = 'All ages admitted.',
                order = 1
            )
        else:
            return CertificationsTvList200ResponseCertificationsITInner(
        )
        """

    def testCertificationsTvList200ResponseCertificationsITInner(self):
        """Test CertificationsTvList200ResponseCertificationsITInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

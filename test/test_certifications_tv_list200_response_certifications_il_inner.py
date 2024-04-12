# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.certifications_tv_list200_response_certifications_il_inner import CertificationsTvList200ResponseCertificationsILInner

class TestCertificationsTvList200ResponseCertificationsILInner(unittest.TestCase):
    """CertificationsTvList200ResponseCertificationsILInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationsTvList200ResponseCertificationsILInner:
        """Test CertificationsTvList200ResponseCertificationsILInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationsTvList200ResponseCertificationsILInner`
        """
        model = CertificationsTvList200ResponseCertificationsILInner()
        if include_optional:
            return CertificationsTvList200ResponseCertificationsILInner(
                certification = 'E',
                meaning = 'Exempt from classification. This rating is usually applied to live broadcasts.',
                order = 1
            )
        else:
            return CertificationsTvList200ResponseCertificationsILInner(
        )
        """

    def testCertificationsTvList200ResponseCertificationsILInner(self):
        """Test CertificationsTvList200ResponseCertificationsILInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.certifications_tv_list200_response_certifications_ma_inner import CertificationsTvList200ResponseCertificationsMAInner

class TestCertificationsTvList200ResponseCertificationsMAInner(unittest.TestCase):
    """CertificationsTvList200ResponseCertificationsMAInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationsTvList200ResponseCertificationsMAInner:
        """Test CertificationsTvList200ResponseCertificationsMAInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationsTvList200ResponseCertificationsMAInner`
        """
        model = CertificationsTvList200ResponseCertificationsMAInner()
        if include_optional:
            return CertificationsTvList200ResponseCertificationsMAInner(
                certification = 'NR',
                meaning = 'All audiences.',
                order = 0
            )
        else:
            return CertificationsTvList200ResponseCertificationsMAInner(
        )
        """

    def testCertificationsTvList200ResponseCertificationsMAInner(self):
        """Test CertificationsTvList200ResponseCertificationsMAInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

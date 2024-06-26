# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.certifications_tv_list200_response_certifications_au_inner import CertificationsTvList200ResponseCertificationsAUInner

class TestCertificationsTvList200ResponseCertificationsAUInner(unittest.TestCase):
    """CertificationsTvList200ResponseCertificationsAUInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationsTvList200ResponseCertificationsAUInner:
        """Test CertificationsTvList200ResponseCertificationsAUInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationsTvList200ResponseCertificationsAUInner`
        """
        model = CertificationsTvList200ResponseCertificationsAUInner()
        if include_optional:
            return CertificationsTvList200ResponseCertificationsAUInner(
                certification = 'P',
                meaning = 'Programming is intended for younger children 2–11; commercial stations must show at least 30 minutes of P-rated content each weekday and weekends at all times. No advertisements may be shown during P-rated programs.',
                order = 1
            )
        else:
            return CertificationsTvList200ResponseCertificationsAUInner(
        )
        """

    def testCertificationsTvList200ResponseCertificationsAUInner(self):
        """Test CertificationsTvList200ResponseCertificationsAUInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

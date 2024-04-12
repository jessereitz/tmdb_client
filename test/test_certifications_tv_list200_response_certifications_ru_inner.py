# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.certifications_tv_list200_response_certifications_ru_inner import CertificationsTvList200ResponseCertificationsRUInner

class TestCertificationsTvList200ResponseCertificationsRUInner(unittest.TestCase):
    """CertificationsTvList200ResponseCertificationsRUInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationsTvList200ResponseCertificationsRUInner:
        """Test CertificationsTvList200ResponseCertificationsRUInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationsTvList200ResponseCertificationsRUInner`
        """
        model = CertificationsTvList200ResponseCertificationsRUInner()
        if include_optional:
            return CertificationsTvList200ResponseCertificationsRUInner(
                certification = '16+',
                meaning = 'Only teens the age of 16 or older can watch.',
                order = 4
            )
        else:
            return CertificationsTvList200ResponseCertificationsRUInner(
        )
        """

    def testCertificationsTvList200ResponseCertificationsRUInner(self):
        """Test CertificationsTvList200ResponseCertificationsRUInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
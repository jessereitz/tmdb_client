# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.certification_movie_list200_response_certifications_ca_inner import CertificationMovieList200ResponseCertificationsCAInner

class TestCertificationMovieList200ResponseCertificationsCAInner(unittest.TestCase):
    """CertificationMovieList200ResponseCertificationsCAInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationMovieList200ResponseCertificationsCAInner:
        """Test CertificationMovieList200ResponseCertificationsCAInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationMovieList200ResponseCertificationsCAInner`
        """
        model = CertificationMovieList200ResponseCertificationsCAInner()
        if include_optional:
            return CertificationMovieList200ResponseCertificationsCAInner(
                certification = 'G',
                meaning = 'All ages.',
                order = 2
            )
        else:
            return CertificationMovieList200ResponseCertificationsCAInner(
        )
        """

    def testCertificationMovieList200ResponseCertificationsCAInner(self):
        """Test CertificationMovieList200ResponseCertificationsCAInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
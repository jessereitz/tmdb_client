# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.certification_movie_list200_response_certifications_jp_inner import CertificationMovieList200ResponseCertificationsJPInner

class TestCertificationMovieList200ResponseCertificationsJPInner(unittest.TestCase):
    """CertificationMovieList200ResponseCertificationsJPInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationMovieList200ResponseCertificationsJPInner:
        """Test CertificationMovieList200ResponseCertificationsJPInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationMovieList200ResponseCertificationsJPInner`
        """
        model = CertificationMovieList200ResponseCertificationsJPInner()
        if include_optional:
            return CertificationMovieList200ResponseCertificationsJPInner(
                certification = 'G',
                meaning = 'General, suitable for all ages.',
                order = 1
            )
        else:
            return CertificationMovieList200ResponseCertificationsJPInner(
        )
        """

    def testCertificationMovieList200ResponseCertificationsJPInner(self):
        """Test CertificationMovieList200ResponseCertificationsJPInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

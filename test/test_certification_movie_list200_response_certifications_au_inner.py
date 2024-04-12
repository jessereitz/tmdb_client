# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.certification_movie_list200_response_certifications_au_inner import CertificationMovieList200ResponseCertificationsAUInner

class TestCertificationMovieList200ResponseCertificationsAUInner(unittest.TestCase):
    """CertificationMovieList200ResponseCertificationsAUInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationMovieList200ResponseCertificationsAUInner:
        """Test CertificationMovieList200ResponseCertificationsAUInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationMovieList200ResponseCertificationsAUInner`
        """
        model = CertificationMovieList200ResponseCertificationsAUInner()
        if include_optional:
            return CertificationMovieList200ResponseCertificationsAUInner(
                certification = 'E',
                meaning = 'Exempt from classification. Films that are exempt from classification must not contain contentious material (i.e. material that would ordinarily be rated M or higher).',
                order = 1
            )
        else:
            return CertificationMovieList200ResponseCertificationsAUInner(
        )
        """

    def testCertificationMovieList200ResponseCertificationsAUInner(self):
        """Test CertificationMovieList200ResponseCertificationsAUInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

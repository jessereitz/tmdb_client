# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.certification_movie_list200_response_certifications_in_inner import CertificationMovieList200ResponseCertificationsINInner

class TestCertificationMovieList200ResponseCertificationsINInner(unittest.TestCase):
    """CertificationMovieList200ResponseCertificationsINInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationMovieList200ResponseCertificationsINInner:
        """Test CertificationMovieList200ResponseCertificationsINInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationMovieList200ResponseCertificationsINInner`
        """
        model = CertificationMovieList200ResponseCertificationsINInner()
        if include_optional:
            return CertificationMovieList200ResponseCertificationsINInner(
                certification = 'U',
                meaning = 'Unrestricted Public Exhibition throughout India, suitable for all age groups. Films under this category should not upset children over 4. Such films may contain educational, social or family-oriented themes. Films under this category may also contain fantasy violence and/or mild bad language.',
                order = 1
            )
        else:
            return CertificationMovieList200ResponseCertificationsINInner(
        )
        """

    def testCertificationMovieList200ResponseCertificationsINInner(self):
        """Test CertificationMovieList200ResponseCertificationsINInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

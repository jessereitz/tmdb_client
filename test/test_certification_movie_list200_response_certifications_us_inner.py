# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.certification_movie_list200_response_certifications_us_inner import CertificationMovieList200ResponseCertificationsUSInner

class TestCertificationMovieList200ResponseCertificationsUSInner(unittest.TestCase):
    """CertificationMovieList200ResponseCertificationsUSInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationMovieList200ResponseCertificationsUSInner:
        """Test CertificationMovieList200ResponseCertificationsUSInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationMovieList200ResponseCertificationsUSInner`
        """
        model = CertificationMovieList200ResponseCertificationsUSInner()
        if include_optional:
            return CertificationMovieList200ResponseCertificationsUSInner(
                certification = 'R',
                meaning = 'Under 17 requires accompanying parent or adult guardian 21 or older. The parent/guardian is required to stay with the child under 17 through the entire movie, even if the parent gives the child/teenager permission to see the film alone. These films may contain strong profanity, graphic sexuality, nudity, strong violence, horror, gore, and strong drug use. A movie rated R for profanity often has more severe or frequent language than the PG-13 rating would permit. An R-rated movie may have more blood, gore, drug use, nudity, or graphic sexuality than a PG-13 movie would admit.',
                order = 4
            )
        else:
            return CertificationMovieList200ResponseCertificationsUSInner(
        )
        """

    def testCertificationMovieList200ResponseCertificationsUSInner(self):
        """Test CertificationMovieList200ResponseCertificationsUSInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
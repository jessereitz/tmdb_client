# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.credit_details200_response_media_seasons_inner import CreditDetails200ResponseMediaSeasonsInner

class TestCreditDetails200ResponseMediaSeasonsInner(unittest.TestCase):
    """CreditDetails200ResponseMediaSeasonsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreditDetails200ResponseMediaSeasonsInner:
        """Test CreditDetails200ResponseMediaSeasonsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreditDetails200ResponseMediaSeasonsInner`
        """
        model = CreditDetails200ResponseMediaSeasonsInner()
        if include_optional:
            return CreditDetails200ResponseMediaSeasonsInner(
                air_date = '2023-01-15',
                episode_count = 9,
                id = 144593,
                name = 'Staffel 1',
                overview = 'Die 1. Staffel der Endzeit-Horrorserie The Last of Us feierte ihre Premiere am 15. Januar 2023 bei HBO. In Staffel 1 beginnt für den Überlebenden Joel und das Mädchen Ellie eine Reise durch das postapokalyptische Amerika, in dem Plünderer und mutierte Wesen ihnen nach dem Leben trachten.',
                poster_path = '/aUQKIpZZ31KWbpdHMCmaV76u78T.jpg',
                season_number = 1,
                show_id = 100088
            )
        else:
            return CreditDetails200ResponseMediaSeasonsInner(
        )
        """

    def testCreditDetails200ResponseMediaSeasonsInner(self):
        """Test CreditDetails200ResponseMediaSeasonsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_aggregate_credits200_response_cast_inner_roles_inner import TvSeriesAggregateCredits200ResponseCastInnerRolesInner

class TestTvSeriesAggregateCredits200ResponseCastInnerRolesInner(unittest.TestCase):
    """TvSeriesAggregateCredits200ResponseCastInnerRolesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesAggregateCredits200ResponseCastInnerRolesInner:
        """Test TvSeriesAggregateCredits200ResponseCastInnerRolesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesAggregateCredits200ResponseCastInnerRolesInner`
        """
        model = TvSeriesAggregateCredits200ResponseCastInnerRolesInner()
        if include_optional:
            return TvSeriesAggregateCredits200ResponseCastInnerRolesInner(
                credit_id = '5256c8af19c2956ff60479f6',
                character = 'Daenerys Targaryen',
                episode_count = 78
            )
        else:
            return TvSeriesAggregateCredits200ResponseCastInnerRolesInner(
        )
        """

    def testTvSeriesAggregateCredits200ResponseCastInnerRolesInner(self):
        """Test TvSeriesAggregateCredits200ResponseCastInnerRolesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

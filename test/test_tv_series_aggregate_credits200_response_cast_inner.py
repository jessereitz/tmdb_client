# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_aggregate_credits200_response_cast_inner import TvSeriesAggregateCredits200ResponseCastInner

class TestTvSeriesAggregateCredits200ResponseCastInner(unittest.TestCase):
    """TvSeriesAggregateCredits200ResponseCastInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesAggregateCredits200ResponseCastInner:
        """Test TvSeriesAggregateCredits200ResponseCastInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesAggregateCredits200ResponseCastInner`
        """
        model = TvSeriesAggregateCredits200ResponseCastInner()
        if include_optional:
            return TvSeriesAggregateCredits200ResponseCastInner(
                adult = False,
                gender = 1,
                id = 1223786,
                known_for_department = 'Acting',
                name = 'Emilia Clarke',
                original_name = 'Emilia Clarke',
                popularity = 42.737,
                profile_path = '/u59kTmNHXzaGZqokivxLPiBVIML.jpg',
                roles = [
                    tmdb_client.models.tv_series_aggregate_credits_200_response_cast_inner_roles_inner.tv_series_aggregate_credits_200_response_cast_inner_roles_inner(
                        credit_id = '5256c8af19c2956ff60479f6', 
                        character = 'Daenerys Targaryen', 
                        episode_count = 78, )
                    ],
                total_episode_count = 78,
                order = 6
            )
        else:
            return TvSeriesAggregateCredits200ResponseCastInner(
        )
        """

    def testTvSeriesAggregateCredits200ResponseCastInner(self):
        """Test TvSeriesAggregateCredits200ResponseCastInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

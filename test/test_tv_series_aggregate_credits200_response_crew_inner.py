# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_aggregate_credits200_response_crew_inner import TvSeriesAggregateCredits200ResponseCrewInner

class TestTvSeriesAggregateCredits200ResponseCrewInner(unittest.TestCase):
    """TvSeriesAggregateCredits200ResponseCrewInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesAggregateCredits200ResponseCrewInner:
        """Test TvSeriesAggregateCredits200ResponseCrewInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesAggregateCredits200ResponseCrewInner`
        """
        model = TvSeriesAggregateCredits200ResponseCrewInner()
        if include_optional:
            return TvSeriesAggregateCredits200ResponseCrewInner(
                adult = False,
                gender = 1,
                id = 6411,
                known_for_department = 'Art',
                name = 'Deborah Riley',
                original_name = 'Deborah Riley',
                popularity = 1.4,
                profile_path = '/cjhADpqdrnwB1PdDUKaBnWrIj2Q.jpg',
                jobs = [
                    tmdb_client.models.tv_series_aggregate_credits_200_response_crew_inner_jobs_inner.tv_series_aggregate_credits_200_response_crew_inner_jobs_inner(
                        credit_id = '54eee9e5c3a3686d5800584e', 
                        job = 'Production Design', 
                        episode_count = 43, )
                    ],
                department = 'Art',
                total_episode_count = 43
            )
        else:
            return TvSeriesAggregateCredits200ResponseCrewInner(
        )
        """

    def testTvSeriesAggregateCredits200ResponseCrewInner(self):
        """Test TvSeriesAggregateCredits200ResponseCrewInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

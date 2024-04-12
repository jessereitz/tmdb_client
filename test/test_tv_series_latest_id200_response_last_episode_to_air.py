# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_latest_id200_response_last_episode_to_air import TvSeriesLatestId200ResponseLastEpisodeToAir

class TestTvSeriesLatestId200ResponseLastEpisodeToAir(unittest.TestCase):
    """TvSeriesLatestId200ResponseLastEpisodeToAir unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesLatestId200ResponseLastEpisodeToAir:
        """Test TvSeriesLatestId200ResponseLastEpisodeToAir
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesLatestId200ResponseLastEpisodeToAir`
        """
        model = TvSeriesLatestId200ResponseLastEpisodeToAir()
        if include_optional:
            return TvSeriesLatestId200ResponseLastEpisodeToAir(
                id = 4398801,
                name = 'Episode 8',
                overview = '',
                vote_average = 0,
                vote_count = 0,
                air_date = '2023-04-21',
                episode_number = 8,
                production_code = '',
                runtime = None,
                season_number = 1,
                show_id = 225491,
                still_path = None
            )
        else:
            return TvSeriesLatestId200ResponseLastEpisodeToAir(
        )
        """

    def testTvSeriesLatestId200ResponseLastEpisodeToAir(self):
        """Test TvSeriesLatestId200ResponseLastEpisodeToAir"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
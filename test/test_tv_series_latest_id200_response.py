# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_latest_id200_response import TvSeriesLatestId200Response

class TestTvSeriesLatestId200Response(unittest.TestCase):
    """TvSeriesLatestId200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesLatestId200Response:
        """Test TvSeriesLatestId200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesLatestId200Response`
        """
        model = TvSeriesLatestId200Response()
        if include_optional:
            return TvSeriesLatestId200Response(
                adult = False,
                backdrop_path = None,
                created_by = [
                    ''
                    ],
                episode_run_time = [
                    ''
                    ],
                first_air_date = '',
                genres = [
                    ''
                    ],
                homepage = '',
                id = 225491,
                in_production = True,
                languages = [
                    ''
                    ],
                last_air_date = '2023-04-21',
                last_episode_to_air = tmdb_client.models.tv_series_latest_id_200_response_last_episode_to_air.tv_series_latest_id_200_response_last_episode_to_air(
                    id = 4398801, 
                    name = 'Episode 8', 
                    overview = '', 
                    vote_average = 0, 
                    vote_count = 0, 
                    air_date = '2023-04-21', 
                    episode_number = 8, 
                    production_code = '', 
                    runtime = null, 
                    season_number = 1, 
                    show_id = 225491, 
                    still_path = null, ),
                name = '妖怪传',
                next_episode_to_air = None,
                networks = [
                    ''
                    ],
                number_of_episodes = 1,
                number_of_seasons = 1,
                origin_country = [
                    'CN'
                    ],
                original_language = 'zh',
                original_name = '妖怪传',
                overview = '',
                popularity = 0,
                poster_path = None,
                production_companies = [
                    ''
                    ],
                production_countries = [
                    ''
                    ],
                seasons = [
                    tmdb_client.models.tv_series_latest_id_200_response_seasons_inner.tv_series_latest_id_200_response_seasons_inner(
                        air_date = null, 
                        episode_count = 1, 
                        id = 338956, 
                        name = 'Season 1', 
                        overview = '', 
                        poster_path = null, 
                        season_number = 1, )
                    ],
                spoken_languages = [
                    ''
                    ],
                status = 'Returning Series',
                tagline = '',
                type = 'Scripted',
                vote_average = 0,
                vote_count = 0
            )
        else:
            return TvSeriesLatestId200Response(
        )
        """

    def testTvSeriesLatestId200Response(self):
        """Test TvSeriesLatestId200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

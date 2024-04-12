# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.find_by_id200_response import FindById200Response

class TestFindById200Response(unittest.TestCase):
    """FindById200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FindById200Response:
        """Test FindById200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FindById200Response`
        """
        model = FindById200Response()
        if include_optional:
            return FindById200Response(
                movie_results = [
                    openapi_client.models.find_by_id_200_response_movie_results_inner.find_by_id_200_response_movie_results_inner(
                        adult = False, 
                        backdrop_path = '/44immBwzhDVyjn87b3x3l9mlhAD.jpg', 
                        id = 934433, 
                        title = 'Scream VI', 
                        original_language = 'en', 
                        original_title = 'Scream VI', 
                        overview = 'Following the latest Ghostface killings, the four survivors leave Woodsboro behind and start a fresh chapter.', 
                        poster_path = '/wDWwtvkRRlgTiUr6TyLSMX8FCuZ.jpg', 
                        media_type = 'movie', 
                        genre_ids = [
                            27
                            ], 
                        popularity = 853.917, 
                        release_date = '2023-03-08', 
                        video = False, 
                        vote_average = 7.388, 
                        vote_count = 708, )
                    ],
                person_results = [
                    ''
                    ],
                tv_results = [
                    ''
                    ],
                tv_episode_results = [
                    ''
                    ],
                tv_season_results = [
                    ''
                    ]
            )
        else:
            return FindById200Response(
        )
        """

    def testFindById200Response(self):
        """Test FindById200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

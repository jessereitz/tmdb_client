# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_episode_images200_response import TvEpisodeImages200Response

class TestTvEpisodeImages200Response(unittest.TestCase):
    """TvEpisodeImages200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvEpisodeImages200Response:
        """Test TvEpisodeImages200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvEpisodeImages200Response`
        """
        model = TvEpisodeImages200Response()
        if include_optional:
            return TvEpisodeImages200Response(
                id = 63056,
                stills = [
                    tmdb_client.models.tv_episode_images_200_response_stills_inner.tv_episode_images_200_response_stills_inner(
                        aspect_ratio = 1.778, 
                        height = 1080, 
                        iso_639_1 = null, 
                        file_path = '/9hGF3WUkBf7cSjMg0cdMDHJkByd.jpg', 
                        vote_average = 5.454, 
                        vote_count = 3, 
                        width = 1920, )
                    ]
            )
        else:
            return TvEpisodeImages200Response(
        )
        """

    def testTvEpisodeImages200Response(self):
        """Test TvEpisodeImages200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

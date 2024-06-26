# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_episode_changes_by_id200_response_changes_inner import TvEpisodeChangesById200ResponseChangesInner

class TestTvEpisodeChangesById200ResponseChangesInner(unittest.TestCase):
    """TvEpisodeChangesById200ResponseChangesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvEpisodeChangesById200ResponseChangesInner:
        """Test TvEpisodeChangesById200ResponseChangesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvEpisodeChangesById200ResponseChangesInner`
        """
        model = TvEpisodeChangesById200ResponseChangesInner()
        if include_optional:
            return TvEpisodeChangesById200ResponseChangesInner(
                key = 'production_code',
                items = [
                    tmdb_client.models.tv_episode_changes_by_id_200_response_changes_inner_items_inner.tv_episode_changes_by_id_200_response_changes_inner_items_inner(
                        id = '54bd9ed7c3a3686c6b00da66', 
                        action = 'added', 
                        time = '2015-01-20 00:18:31 UTC', 
                        value = '101', )
                    ]
            )
        else:
            return TvEpisodeChangesById200ResponseChangesInner(
        )
        """

    def testTvEpisodeChangesById200ResponseChangesInner(self):
        """Test TvEpisodeChangesById200ResponseChangesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

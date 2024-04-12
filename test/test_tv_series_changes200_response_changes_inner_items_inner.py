# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_changes200_response_changes_inner_items_inner import TvSeriesChanges200ResponseChangesInnerItemsInner

class TestTvSeriesChanges200ResponseChangesInnerItemsInner(unittest.TestCase):
    """TvSeriesChanges200ResponseChangesInnerItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesChanges200ResponseChangesInnerItemsInner:
        """Test TvSeriesChanges200ResponseChangesInnerItemsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesChanges200ResponseChangesInnerItemsInner`
        """
        model = TvSeriesChanges200ResponseChangesInnerItemsInner()
        if include_optional:
            return TvSeriesChanges200ResponseChangesInnerItemsInner(
                id = '640435cf021cee0084710972',
                action = 'updated',
                time = '2023-03-05 06:25:19 UTC',
                iso_639_1 = 'en',
                iso_3166_1 = '',
                value = openapi_client.models.tv_series_changes_200_response_changes_inner_items_inner_value.tv_series_changes_200_response_changes_inner_items_inner_value(
                    poster = openapi_client.models.tv_series_changes_200_response_changes_inner_items_inner_value_poster.tv_series_changes_200_response_changes_inner_items_inner_value_poster(
                        file_path = '/ouudK6RCNnsbT1CSXrlATXQIQTG.jpg', 
                        iso_639_1 = 'en', ), ),
                original_value = openapi_client.models.tv_series_changes_200_response_changes_inner_items_inner_original_value.tv_series_changes_200_response_changes_inner_items_inner_original_value(
                    poster = openapi_client.models.tv_series_changes_200_response_changes_inner_items_inner_original_value_poster.tv_series_changes_200_response_changes_inner_items_inner_original_value_poster(
                        file_path = '/ouudK6RCNnsbT1CSXrlATXQIQTG.jpg', 
                        iso_639_1 = 'fr', ), )
            )
        else:
            return TvSeriesChanges200ResponseChangesInnerItemsInner(
        )
        """

    def testTvSeriesChanges200ResponseChangesInnerItemsInner(self):
        """Test TvSeriesChanges200ResponseChangesInnerItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
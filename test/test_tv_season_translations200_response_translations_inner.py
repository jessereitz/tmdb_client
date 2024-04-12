# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_season_translations200_response_translations_inner import TvSeasonTranslations200ResponseTranslationsInner

class TestTvSeasonTranslations200ResponseTranslationsInner(unittest.TestCase):
    """TvSeasonTranslations200ResponseTranslationsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeasonTranslations200ResponseTranslationsInner:
        """Test TvSeasonTranslations200ResponseTranslationsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeasonTranslations200ResponseTranslationsInner`
        """
        model = TvSeasonTranslations200ResponseTranslationsInner()
        if include_optional:
            return TvSeasonTranslations200ResponseTranslationsInner(
                iso_3166_1 = 'SA',
                iso_639_1 = 'ar',
                name = 'العربية',
                english_name = 'Arabic',
                data = tmdb_client.models.tv_season_translations_200_response_translations_inner_data.tv_season_translations_200_response_translations_inner_data(
                    name = '', 
                    overview = 'سلسلة درامية مبنية على سلسلة روايات لـ جورج آر آر مارتن بعنوان "إيه سونغ أوف آيس أن فاير" والتي حققت مبيعات كبيرة وتتمحور حول الصراعات التي كانت تحدث في العصور الوسطى بين العائلات النبيلة للسيطرة على عرش وستيروس.', )
            )
        else:
            return TvSeasonTranslations200ResponseTranslationsInner(
        )
        """

    def testTvSeasonTranslations200ResponseTranslationsInner(self):
        """Test TvSeasonTranslations200ResponseTranslationsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

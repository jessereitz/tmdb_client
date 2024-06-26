# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_translations200_response_translations_inner import TvSeriesTranslations200ResponseTranslationsInner

class TestTvSeriesTranslations200ResponseTranslationsInner(unittest.TestCase):
    """TvSeriesTranslations200ResponseTranslationsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesTranslations200ResponseTranslationsInner:
        """Test TvSeriesTranslations200ResponseTranslationsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesTranslations200ResponseTranslationsInner`
        """
        model = TvSeriesTranslations200ResponseTranslationsInner()
        if include_optional:
            return TvSeriesTranslations200ResponseTranslationsInner(
                iso_3166_1 = 'SA',
                iso_639_1 = 'ar',
                name = 'العربية',
                english_name = 'Arabic',
                data = tmdb_client.models.tv_series_translations_200_response_translations_inner_data.tv_series_translations_200_response_translations_inner_data(
                    name = 'صراع العروش', 
                    overview = 'تتقاتل سبع عائلات نبيلة من أجل السيطرة على أرض - ويستيروس - الأسطورية. الاحتكاك بين العوائل يؤدي إلى حرب واسعة النطاق.  في حين يستيقظ الشر القديم في أقصى الشمال. وفي خضم الحرب، نظام عسكري مهمَل - حرس الليل - هم كل ما يقف بين عالم الإنسان والأهوال الجليدية.', 
                    homepage = '', 
                    tagline = 'الشتاء قادم', )
            )
        else:
            return TvSeriesTranslations200ResponseTranslationsInner(
        )
        """

    def testTvSeriesTranslations200ResponseTranslationsInner(self):
        """Test TvSeriesTranslations200ResponseTranslationsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

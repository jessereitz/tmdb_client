# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_translations200_response_translations_inner import MovieTranslations200ResponseTranslationsInner

class TestMovieTranslations200ResponseTranslationsInner(unittest.TestCase):
    """MovieTranslations200ResponseTranslationsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieTranslations200ResponseTranslationsInner:
        """Test MovieTranslations200ResponseTranslationsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieTranslations200ResponseTranslationsInner`
        """
        model = MovieTranslations200ResponseTranslationsInner()
        if include_optional:
            return MovieTranslations200ResponseTranslationsInner(
                iso_3166_1 = 'SA',
                iso_639_1 = 'ar',
                name = 'العربية',
                english_name = 'Arabic',
                data = tmdb_client.models.movie_translations_200_response_translations_inner_data.movie_translations_200_response_translations_inner_data(
                    homepage = '', 
                    overview = 'إدوارد يتعرض لضغوط حتى يصل به الحال إلى أنه لا يستطيع النوم لفتراتٍ طويلة، لكنه يجد بعض السلام في جلسات العلاج النفسي الجماعي، يتعرف إدوارد على أحد الأشخاص وهو (تايلر ديردن) الذي يحرره من تعلقه بالأشياء الذي تستعبده ،ثم يحرره من خوفه من الناس. يقومان معًا بإنشاء نادي القتال الذي يجذب الكثير من الأفراد المحبطين ،الذين يقومون بإخراج طاقة غضبهم وكرههم للعالم في القتال.', 
                    runtime = 0, 
                    tagline = '', 
                    title = '', )
            )
        else:
            return MovieTranslations200ResponseTranslationsInner(
        )
        """

    def testMovieTranslations200ResponseTranslationsInner(self):
        """Test MovieTranslations200ResponseTranslationsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

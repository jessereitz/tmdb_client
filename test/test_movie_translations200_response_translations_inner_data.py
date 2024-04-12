# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_translations200_response_translations_inner_data import MovieTranslations200ResponseTranslationsInnerData

class TestMovieTranslations200ResponseTranslationsInnerData(unittest.TestCase):
    """MovieTranslations200ResponseTranslationsInnerData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieTranslations200ResponseTranslationsInnerData:
        """Test MovieTranslations200ResponseTranslationsInnerData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieTranslations200ResponseTranslationsInnerData`
        """
        model = MovieTranslations200ResponseTranslationsInnerData()
        if include_optional:
            return MovieTranslations200ResponseTranslationsInnerData(
                homepage = '',
                overview = 'إدوارد يتعرض لضغوط حتى يصل به الحال إلى أنه لا يستطيع النوم لفتراتٍ طويلة، لكنه يجد بعض السلام في جلسات العلاج النفسي الجماعي، يتعرف إدوارد على أحد الأشخاص وهو (تايلر ديردن) الذي يحرره من تعلقه بالأشياء الذي تستعبده ،ثم يحرره من خوفه من الناس. يقومان معًا بإنشاء نادي القتال الذي يجذب الكثير من الأفراد المحبطين ،الذين يقومون بإخراج طاقة غضبهم وكرههم للعالم في القتال.',
                runtime = 0,
                tagline = '',
                title = ''
            )
        else:
            return MovieTranslations200ResponseTranslationsInnerData(
        )
        """

    def testMovieTranslations200ResponseTranslationsInnerData(self):
        """Test MovieTranslations200ResponseTranslationsInnerData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.person_combined_credits200_response import PersonCombinedCredits200Response

class TestPersonCombinedCredits200Response(unittest.TestCase):
    """PersonCombinedCredits200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonCombinedCredits200Response:
        """Test PersonCombinedCredits200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonCombinedCredits200Response`
        """
        model = PersonCombinedCredits200Response()
        if include_optional:
            return PersonCombinedCredits200Response(
                cast = [
                    tmdb_client.models.person_combined_credits_200_response_cast_inner.person_combined_credits_200_response_cast_inner(
                        adult = False, 
                        backdrop_path = '/3h1JZGDhZ8nzxdgvkxha0qBqi05.jpg', 
                        genre_ids = [
                            35
                            ], 
                        id = 13, 
                        original_language = 'en', 
                        original_title = 'Forrest Gump', 
                        overview = 'A man with a low IQ has accomplished great things in his life and been present during significant historic events—in each case, far exceeding what anyone imagined he could do. But despite all he has achieved, his one true love eludes him.', 
                        popularity = 62.225, 
                        poster_path = '/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg', 
                        release_date = '1994-06-23', 
                        title = 'Forrest Gump', 
                        video = False, 
                        vote_average = 8.481, 
                        vote_count = 24535, 
                        character = 'Forrest Gump', 
                        credit_id = '52fe420ec3a36847f800074f', 
                        order = 0, 
                        media_type = 'movie', )
                    ],
                crew = [
                    tmdb_client.models.person_combined_credits_200_response_crew_inner.person_combined_credits_200_response_crew_inner(
                        adult = False, 
                        backdrop_path = '/tx3uj8GPWf5pzb0gWATJ4bokNHI.jpg', 
                        genre_ids = [
                            99
                            ], 
                        id = 87061, 
                        original_language = 'fr', 
                        original_title = 'Le Voyage extraordinaire', 
                        overview = 'An account of the extraordinary life of film pioneer Georges Méliès (1861-1938) and the amazing story of the copy in color of his masterpiece “A Trip to the Moon” (1902), unexpectedly found in Spain and restored thanks to the heroic efforts of a group of true cinema lovers.', 
                        popularity = 6.007, 
                        poster_path = '/zHNNT9gfiGsuadR6x38KYOp6ekq.jpg', 
                        release_date = '2011-12-08', 
                        title = 'The Extraordinary Voyage', 
                        video = False, 
                        vote_average = 7.6, 
                        vote_count = 47, 
                        credit_id = '5d818a63d34eb3002c4f8fea', 
                        department = 'Crew', 
                        job = 'Thanks', 
                        media_type = 'movie', )
                    ],
                id = 31
            )
        else:
            return PersonCombinedCredits200Response(
        )
        """

    def testPersonCombinedCredits200Response(self):
        """Test PersonCombinedCredits200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

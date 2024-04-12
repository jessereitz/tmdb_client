# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.person_popular_list200_response_results_inner import PersonPopularList200ResponseResultsInner

class TestPersonPopularList200ResponseResultsInner(unittest.TestCase):
    """PersonPopularList200ResponseResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonPopularList200ResponseResultsInner:
        """Test PersonPopularList200ResponseResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonPopularList200ResponseResultsInner`
        """
        model = PersonPopularList200ResponseResultsInner()
        if include_optional:
            return PersonPopularList200ResponseResultsInner(
                adult = False,
                gender = 1,
                id = 224513,
                known_for = [
                    tmdb_client.models.person_popular_list_200_response_results_inner_known_for_inner.person_popular_list_200_response_results_inner_known_for_inner(
                        adult = False, 
                        backdrop_path = '/ilRyazdMJwN05exqhwK4tMKBYZs.jpg', 
                        genre_ids = [
                            878
                            ], 
                        id = 335984, 
                        media_type = 'movie', 
                        original_language = 'en', 
                        original_title = 'Blade Runner 2049', 
                        overview = 'Thirty years after the events of the first film, a new blade runner, LAPD Officer K, unearths a long-buried secret that has the potential to plunge what's left of society into chaos. K's discovery leads him on a quest to find Rick Deckard, a former LAPD blade runner who has been missing for 30 years.', 
                        poster_path = '/gajva2L0rPYkEWjzgFlBXCAVBE5.jpg', 
                        release_date = '2017-10-04', 
                        title = 'Blade Runner 2049', 
                        video = False, 
                        vote_average = 7.5, 
                        vote_count = 11771, )
                    ],
                known_for_department = 'Acting',
                name = 'Ana de Armas',
                popularity = 343.33,
                profile_path = '/3vxvsmYLTf4jnr163SUlBIw51ee.jpg'
            )
        else:
            return PersonPopularList200ResponseResultsInner(
        )
        """

    def testPersonPopularList200ResponseResultsInner(self):
        """Test PersonPopularList200ResponseResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

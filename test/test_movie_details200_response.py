# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_details200_response import MovieDetails200Response

class TestMovieDetails200Response(unittest.TestCase):
    """MovieDetails200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieDetails200Response:
        """Test MovieDetails200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieDetails200Response`
        """
        model = MovieDetails200Response()
        if include_optional:
            return MovieDetails200Response(
                adult = False,
                backdrop_path = '/hZkgoQYus5vegHoetLkCJzb17zJ.jpg',
                belongs_to_collection = None,
                budget = 63000000,
                genres = [
                    openapi_client.models.movie_details_200_response_genres_inner.movie_details_200_response_genres_inner(
                        id = 18, 
                        name = 'Drama', )
                    ],
                homepage = 'http://www.foxmovies.com/movies/fight-club',
                id = 550,
                imdb_id = 'tt0137523',
                original_language = 'en',
                original_title = 'Fight Club',
                overview = 'A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground "fight clubs" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.',
                popularity = 61.416,
                poster_path = '/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg',
                production_companies = [
                    openapi_client.models.movie_details_200_response_production_companies_inner.movie_details_200_response_production_companies_inner(
                        id = 508, 
                        logo_path = '/7cxRWzi4LsVm4Utfpr1hfARNurT.png', 
                        name = 'Regency Enterprises', 
                        origin_country = 'US', )
                    ],
                production_countries = [
                    openapi_client.models.movie_details_200_response_production_countries_inner.movie_details_200_response_production_countries_inner(
                        iso_3166_1 = 'US', 
                        name = 'United States of America', )
                    ],
                release_date = '1999-10-15',
                revenue = 100853753,
                runtime = 139,
                spoken_languages = [
                    openapi_client.models.movie_details_200_response_spoken_languages_inner.movie_details_200_response_spoken_languages_inner(
                        english_name = 'English', 
                        iso_639_1 = 'en', 
                        name = 'English', )
                    ],
                status = 'Released',
                tagline = 'Mischief. Mayhem. Soap.',
                title = 'Fight Club',
                video = False,
                vote_average = 8.433,
                vote_count = 26280
            )
        else:
            return MovieDetails200Response(
        )
        """

    def testMovieDetails200Response(self):
        """Test MovieDetails200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
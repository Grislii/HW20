from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


def convert_list_to_dict(list):
    dictionary_data = {}
    for i in range(len(list)):
        dictionary_data[i + 1] = list[i]
    return dictionary_data


@pytest.fixture
def director_data():
    d1 = Director(id=1, name="Тейлор Шеридан")
    d2 = Director(id=2, name="Дени Вильнёв")
    d3 = Director(id=3, name="Баз Лурман")
    director_list = [d1, d2, d3]

    return convert_list_to_dict(director_list)


@pytest.fixture
def genre_data():
    g1 = Genre(id=1, name="Семейный")
    g2 = Genre(id=2, name="Документальное")
    g3 = Genre(id=3, name="Вестерн")
    genre_list = [g1, g2, g3]

    return convert_list_to_dict(genre_list)


@pytest.fixture
def movie_data():
    m1 = Movie(id=1, title="Йеллоустоун")
    m2 = Movie(id=2, title="Переступить черту")
    m3 = Movie(id=3, title="Лето")
    movie_list = [m1, m2, m3]

    return convert_list_to_dict(movie_list)


@pytest.fixture
def director_dao(director_data: dict):
    director_dao = DirectorDAO(None)

    director_dao.get_one = MagicMock(side_effect=director_data.get)
    director_dao.get_all = MagicMock(return_value=list(director_data.values()))
    director_dao.create = MagicMock(return_value=director_data[1])
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


@pytest.fixture
def genre_dao(genre_data: dict):
    genre_dao = GenreDAO(None)

    genre_dao.get_one = MagicMock(side_effect=genre_data.get)
    genre_dao.get_all = MagicMock(return_value=list(genre_data.values()))
    genre_dao.create = MagicMock(return_value=genre_data[1])
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


@pytest.fixture
def movie_dao(movie_data: dict):
    movie_dao = MovieDAO(None)

    movie_dao.get_one = MagicMock(side_effect=movie_data.get)
    movie_dao.get_all = MagicMock(return_value=list(movie_data.values()))
    movie_dao.create = MagicMock(return_value=movie_data[1])
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao

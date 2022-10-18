import pytest

from dao.model.movie import Movie
from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(3)
        assert movie.title == "Лето"

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        new_movie = self.movie_service.create(Movie(id=4, title="Ла-Ла Ленд"))
        assert new_movie.title is not None

    def test_update(self):
        result = self.movie_service.update(1)

    def test_delete(self):
        result = self.movie_service.delete(1)
        assert result is None

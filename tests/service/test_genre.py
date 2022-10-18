import pytest

from dao.model.genre import Genre
from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(2)
        assert genre.name == "Документальное"

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        new_genre = self.genre_service.create(Genre(id=4, name="Мюзикл"))
        assert new_genre.name is not None

    def test_update(self):
        result = self.genre_service.update(1)

    def test_delete(self):
        result = self.genre_service.delete(1)
        assert result is None

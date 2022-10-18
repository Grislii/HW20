import pytest

from dao.model.director import Director
from service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director.name == "Тейлор Шеридан"

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        new_director = self.director_service.create(Director(id=4, name="Мор Ларман"))
        assert new_director.name is not None

    def test_update(self):
        result = self.director_service.update(1)

    def test_delete(self):
        result = self.director_service.delete(1)
        assert result is None

import tmdb_client
import requests
from unittest.mock import Mock


def test_get_single_movie(monkeypatch):
    mov_list = ['mov_1', 'mov_2', 'mov_3']
    mov_sing_test = Mock()
    response = mov_sing_test.return_value
    response.json.return_value = mov_list
    monkeypatch.setattr("tmdb_client.requests.get", mov_sing_test)
    movie_list = tmdb_client.get_movies_list(list_type="upcoming")
    assert movie_list == mov_list


def test_get_movie_images(monkeypatch):
    mov_img = ['title', 'tagline', 'overview', 'budget', 'genre']
    mov_img_test = Mock()
    response = mov_img_test.return_value
    response.json.return_value = mov_img
    monkeypatch.setattr("tmdb_client.requests.get", mov_img_test)
    movie = tmdb_client.get_single_movie(movie_id=123)
    assert movie == mov_img


def test_get_single_movie_cast(monkeypatch):
    mov_cast = ['actor1', 'actor2', 'actor3', 'actor4', 'actor5']
    mov_cast_test = Mock()
    response = mov_cast_test.return_value
    response.json.return_value = mov_cast
    monkeypatch.setattr("tmdb_client.requests.get", mov_cast_test)
    movie_cast = tmdb_client.get_single_movie_cast(movie_id=123)
    assert movie_cast == mov_cast


class MockResponse():
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}

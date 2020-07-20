import tmdb_client
from unittest.mock import Mock
import requests
from app import app
import pytest


def test_get_single_movie(monkeypatch):
    mock_movie = ['mov1', 'mov2', 'mov3', 'mov4', 'mov5']
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movie = tmdb_client.get_single_movie(movie_id=1)
    assert movie == mock_movie


def test_get_movie_images(monkeypatch):
    movie_images_mock = ['img1', 'img2', 'img3', 'img4']
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = movie_images_mock
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movie_images = tmdb_client.get_movie_images(movie_id=1)
    assert movie_images == movie_images_mock


class MockResponse():
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


def test_get_json(monkeypatch):

    def mock_get(*args, **kwargs):
        return MockResponse.json()

    monkeypatch.setattr(requests, "get", mock_get)
    result = tmdb_client.requests.get("https://fakeurl")
    assert result["mock_key"] == "mock_response"


def test_get_single_movie_cast(monkeypatch):
    movie_cast_mock = {'cast': 'Ja'}
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = movie_cast_mock
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movie = tmdb_client.get_single_movie_cast(movie_id=1)
    assert movie == movie_cast_mock['cast']


@pytest.mark.parametrize('n, result', (
    ('movie/popular', 200),
    ('movie/now_playing', 200),
    ('movie/top_rated', 200),
    ('movie/upcoming', 200),
))
def test_lists(monkeypatch, n, result):
    api_mock = Mock(return_value={'results': [0, 1, 2, 3]})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)
    with app.test_client(result) as client:
        response = client.get('/')
        assert response.status_code == result
        api_mock.assert_called_once_with(n)

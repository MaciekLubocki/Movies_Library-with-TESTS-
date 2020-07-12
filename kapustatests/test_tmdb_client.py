import requests
import tmdb_client
from unittest.mock import Mock


def test_get_single_movie(monkeypatch):
    get_single_movie_mock = ['title', 'tagline', 'overview', 'budget', 'genre']
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = get_single_movie_mock
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    get_single_movie = tmdb_client.get_single_movie(movie_id=123)
    assert get_single_movie == get_single_movie_mock


class MockResponse():
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}

def test_get_movie_images(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse.json()
    monkeypatch.setattr(requests, "get", mock_get)
    result = tmdb_client.requests.get("https://fakeurl")
    assert result["mock_key"] == "mock_response"

def test_get_single_movie_cast(monkeypatch):
    poster_api_path = "some-poster-path"
    expected_default_size = 'w342'
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    assert expected_default_size in poster_url
    assert str(tmdb_client.get_single_movie_cast(666)) == "https://fakeurl"
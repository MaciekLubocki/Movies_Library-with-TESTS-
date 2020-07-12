import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMWYwMDliNmE5OTYxYTRhMmY0MDQ2YmE3OTU4NjdhNSIsInN1YiI6IjVlZTg4ZmVhNjhiNzY2MDAyM2JhNmRjZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Gasjj-1s35UiWCzTFzH7x0ybmYBDi77vtuHzXsY9kvk"


def head():
    header = {"Authorization": f"Bearer {API_TOKEN}"}
    return header


def get_movies_list(list_type):
    headers = head()
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 404:
        endpoint = f"https://api.themoviedb.org/3/movie/popular"
        response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_single_movie(movie_id):
    headers = head()
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movie_images(movie_id):
    headers = head()
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    response = requests.get(endpoint, headers=headers)
    return response.json()





def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]


def get_popular_movies():
    headers = head()
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_path}"


def get_pic_url(backdrop_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{backdrop_path}"



def get_single_movie_cast(movie_id):
    headers = head()
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]












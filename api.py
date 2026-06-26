import requests
from config import API_KEY, BASE_URL, ENDPOINTS

def fetch_movies(movie_type):
    if not API_KEY:
        print("Error: TMDB_API_KEY is not set in your .env file.")
        exit(1)

    endpoint = ENDPOINTS[movie_type]
    url = f"{BASE_URL}{endpoint}"

    try:
        response = requests.get(url, params={"api_key": API_KEY, "language": "en-US", "page": 1})
        response.raise_for_status()
        data = response.json()
        return data["results"]

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection.")
        exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"API error: {e.response.status_code} - {e.response.reason}")
        exit(1)
    except Exception as e:
        print(f"Something went wrong: {e}")
        exit(1)
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

ENDPOINTS = {
    "playing": "/movie/now_playing",
    "popular": "/movie/popular",
    "top":     "/movie/top_rated",
    "upcoming": "/movie/upcoming",
}
import argparse
from api import fetch_movies

def main():
    parser = argparse.ArgumentParser(description="TMDB CLI Tool — fetch movies from The Movie Database")
    parser.add_argument("--type", required=True, choices=["playing", "popular", "top", "upcoming"],
                        help="Type of movies to fetch: playing, popular, top, upcoming")
    args = parser.parse_args()

    movies = fetch_movies(args.type)

    print(f"\n{'='*60}")
    print(f"  Results for: {args.type.upper()}")
    print(f"{'='*60}\n")

    for i, movie in enumerate(movies, 1):
        year = movie.get("release_date", "N/A")[:4]
        title = movie.get("title", "Unknown")
        rating = movie.get("vote_average", 0)
        overview = movie.get("overview", "No description available.")

        print(f"{i}. {title} ({year}) — ⭐ {rating}/10")
        print(f"   {overview[:120]}...")
        print()

if __name__ == "__main__":
    main()
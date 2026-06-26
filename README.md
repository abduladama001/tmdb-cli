# TMDB CLI Tool

A command-line tool to fetch and display movies from The Movie Database (TMDB).

## Prerequisites
- Python 3.7+
- A TMDB API key — get one free at https://www.themoviedb.org/settings/api

## Installation

1. Clone the repo and enter the directory:
   git clone <your-repo-url>
   cd tmdb-cli

2. Install dependencies:
   pip install -r requirements.txt

3. Add your API key to the .env file:
   TMDB_API_KEY=your_api_key_here

## Usage

python main.py --type "popular"
python main.py --type "playing"
python main.py --type "top"
python main.py --type "upcoming"

## Movie Types

| Argument   | Description        |
|------------|--------------------|
| popular    | Most popular movies |
| playing    | Now playing in theatres |
| top        | Top rated of all time |
| upcoming   | Coming soon |
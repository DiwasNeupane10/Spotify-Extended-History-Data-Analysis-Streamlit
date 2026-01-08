import re
from pathlib import Path
import json
import requests
import pandas as pd
import time
import logging
from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY =os.getenv("API_KEY")
CACHE_FILE = "artist_genres_lastfm.parquet"
SLEEP_TIME = 0.3
TOP_N_TAGS = 1


logging.basicConfig(
    filename="lastfm.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w"
)
logger = logging.getLogger(__name__)



def fetch_artist_tags(artist: str, top_n: int ) -> list:
    url = "http://ws.audioscrobbler.com/2.0/"
    params = {
        "method": "artist.gettoptags",
        "artist": artist,
        "api_key": API_KEY,
        "format": "json"
    }

    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()

        tags = data.get("toptags", {}).get("tag", [])
        logger.info(f'...{artist}:Tag Found {tags[:top_n]}')

        return [tag["name"].lower() for tag in tags[:top_n]]

    except requests.exceptions.RequestException as e:
        logger.error(f"{artist} → API error: {e}")
        return []



def get_artist_genres(artists: pd.Series) -> dict:
    artist_genres = {}

    for artist in artists.dropna().unique():
        genres = fetch_artist_tags(artist, TOP_N_TAGS)

        if genres:
            artist_genres[artist] = genres
        else:
            logger.info(f"{artist} → No tags found")

        time.sleep(SLEEP_TIME)

    return artist_genres



if __name__ == "__main__":
    BASE_DIR = Path(__file__).parent
    df = pd.read_parquet(BASE_DIR / "data/df_streamliit.parquet")

    artists = df["master_metadata_album_artist_name"].drop_duplicates()

    # Load cache if exists
    if Path(CACHE_FILE).exists():
        cached = pd.read_parquet(CACHE_FILE).to_dict()
    else:
        cached = {}


    missing_artists = artists[~artists.isin(cached.keys())]

    print(f"Fetching genres for {len(missing_artists)} new artists...")

    # new_genres = get_artist_genres(missing_artists)




    LOG_FILE = "lastfm.log"
    OUTPUT_FILE = "artist_genres.jsonl"
    def func():

        # Regex to extract: artist name and the tag list dict
        pattern = re.compile(r"- INFO - .*?\.{0,3}(.*?):Tag Found (.+)$")

        lines = Path(LOG_FILE).read_text(encoding="utf-8").splitlines()

        with open(OUTPUT_FILE, "w", encoding="utf-8") as out_f:
            for line in lines:
                match = pattern.search(line)
                if match:
                    artist = match.group(1).strip()
                    tags_str = match.group(2).strip()
                    try:
                        # Convert string representation of list/dict to Python object
                        tags = eval(tags_str)  # safe if you trust your log
                        json_line = json.dumps({"artist": artist, "tags": tags}, ensure_ascii=False)
                        out_f.write(json_line + "\n")
                    except Exception as e:
                        print(f"Failed to parse line for {artist}: {e}")

func()
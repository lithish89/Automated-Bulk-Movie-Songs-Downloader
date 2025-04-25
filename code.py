import os
import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from urllib.parse import urlparse, parse_qs, unquote

# Setup Chrome options
options = Options()
options.add_argument('--headless')  # Run in headless mode (no UI)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Setup Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Read Excel file (no headers)
excel_path = "movies.xlsx"
df = pd.read_excel(excel_path, header=None)
movie_names = df[0].tolist()

# Create a folder to store songs
if not os.path.exists("Downloaded_Songs"):
    os.makedirs("Downloaded_Songs")

def normalize(text):
    return text.lower().replace(" ", "").strip()

for idx, movie in enumerate(movie_names):
    try:
        print(f"\n🎬 Movie: {movie}")
        driver.get("https://naasongs.com.co/")

        # Search for the movie
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(movie)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        # Get all <a> tags and find movie link
        links = driver.find_elements(By.TAG_NAME, "a")
        movie_url = None
        movie_normalized = normalize(movie)

        for link in links:
            link_text = link.text
            href = link.get_attribute("href")

            if not link_text or not href:
                continue

            if movie_normalized in normalize(link_text):
                # Handle Google redirect URLs
                if "google.com/url" in href:
                    parsed = urlparse(href)
                    real_url = parse_qs(parsed.query).get("q", [None])[0]
                    if real_url and "naasongs.com.co" in real_url:
                        movie_url = real_url
                        break
                elif "naasongs.com.co" in href:
                    movie_url = href
                    break

        if not movie_url:
            print(f"❌ No link found for {movie}")
            df.at[idx, 1] = "Incomplete"
            continue

        print(f"🔗 Movie link found: {movie_url}")
        driver.get(movie_url)
        time.sleep(3)

        # Download all songs with 'Download' link text
        download_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Download")
        song_found = False

        for link in download_links:
            song_url = link.get_attribute("href")
            if song_url.endswith(".mp3"):
                song_found = True
                song_name = unquote(song_url.split("/")[-1])  # ✅ decode %20 to space
                song_path = os.path.join("Downloaded_Songs", song_name)

                if not os.path.exists(song_path):
                    response = requests.get(song_url)
                    with open(song_path, 'wb') as f:
                        f.write(response.content)
                    print(f"Downloaded: {song_name}")
                else:
                    print(f"Already exists: {song_name}")

        if not song_found:
            df.at[idx, 1] = "Incomplete"
            print(f"⚠️ No MP3 downloads found for {movie}")

    except Exception as e:
        print(f"Error processing movie {movie}: {e}")
        df.at[idx, 1] = "Incomplete"

# Save updates to the Excel file
df.to_excel(excel_path, index=False, header=False)
driver.quit()

# Movie Songs Downloader 🎶

This Python project streamlines and automates the process of downloading Telugu and other language (if available) movie songs from naasongs.com.co. Using Selenium and an Excel file with movie names, this tool allows you to download songs in bulk with ease, saving you the time and effort of manually searching and downloading each song.


## 🔧 Features

Bulk Movie Search: Automatically searches for multiple movie songs using Google-powered search on naasongs.com.co, based on a list of movie names in an Excel file.

Dynamic Parsing: Handles variations in movie title formatting and retrieves the correct movie page, ensuring accurate song downloads even with different naming conventions.

Efficient MP3 Downloads: Downloads all available .mp3 files listed on the movie’s page in one go, eliminating the need for manual downloads.

Skip Redundant Downloads: Automatically skips songs that are already downloaded, preventing duplicates and saving storage space.

Mark Incomplete Movies: If a movie’s songs are not found or no downloadable songs are available, it marks the movie as Incomplete in the Excel file, helping you track progress.

Time-Saving and Easy: Reduces hours of manual work by automating the entire process, making it easy to download a large number of songs in no time.

## 📁 Files

- `code.py` – The main Python script.
- `movies.xlsx` – Excel file with movie names (1 per row).
- `Downloaded_Songs/` – Output folder for MP3s (auto-created).
- `.gitignore` – Ignore unnecessary files.

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt


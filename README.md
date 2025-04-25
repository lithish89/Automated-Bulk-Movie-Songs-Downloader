# Movie Songs Downloader 🎶

This Python project automates the process of downloading Telugu and other language(if available) movie songs from [naasongs.com.co](https://naasongs.com.co) using Selenium and an Excel file containing movie names.

## 🔧 Features

- Searches for movies using Google-powered search on naasongs.
- Parses the correct movie page even if title formatting varies.
- Downloads all `.mp3` files listed on the movie's page.
- Skips already downloaded files.
- Marks movies as `Incomplete` in the Excel if not found or no songs present.

## 📁 Files

- `code.py` – The main Python script.
- `movies.xlsx` – Excel file with movie names (1 per row).
- `Downloaded_Songs/` – Output folder for MP3s (auto-created).
- `.gitignore` – Ignore unnecessary files.

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt


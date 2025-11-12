# Web Scraping Scripts

A personal repo/project to showcase my web scraping skills that I made

# Scripts

## 1. 5-Star Books Scraper(bookScraping.py)

This Python script scrapes the [Books to Scrape](https://books.toscrape.com/) website to collect all **5-star books** and their prices. Each page is saved to a separate text file in the `books` folder.

## Features

- Scrapes all catalogue pages automatically.
- Extracts **book title** and **price** for books with a 5-star rating.
- Creates **one file per page** with the results.
- Waits 1 minute between pages to be polite to the server.
- Stops when there are no more pages.

## Requirements

- Python 3.x
- Packages:
  - `requests`
  - `beautifulsoup4` (`bs4`)

Install dependencies using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone or download this repository.
2. Go to the scripts directory:
   ```
   cd 1_book_scraping
   ```
3. Run the script:
   ```
   python bookScraping.py
   ```
4. The results will be saved in the `books` folder as `5_star_books_page_X.txt`.

### Each file contains:

- Total number of 5-star books on that page.
- Book title and price.

### Notes

- The script waits 1 minute between scraping pages to avoid overloading the website.
- You can adjust the wait time by changing the time_wait variable in the script.
- Make sure you have a stable internet connection.

### License

This script is for educational purposes only. Please do not scrape sites aggressively or violate their terms of service.

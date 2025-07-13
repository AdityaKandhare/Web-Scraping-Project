# 📚 BookScraper – Web Scraping Project

This is a Python-based CLI tool that scrapes book data from [BooksToScrape.com](http://books.toscrape.com). It extracts key details like book titles, ratings, and prices from multiple pages and optionally sends the results to an email address.

## 🔍 Features

- Scrapes book titles, star ratings, and prices from the website
- Supports scraping multiple pages (1–50) interactively
- Outputs results in a clean format to the console
- Optionally emails the results using SMTP
- Easy to run and customize

## 🛠️ Tech Stack

- Python 3
- BeautifulSoup
- Requests
- smtplib / email.mime

## 🚀 How It Works

1. The user selects how many pages (1–50) they want to scrape.
2. The script fetches each page and parses the HTML using BeautifulSoup.
3. Book details (title, rating, cost) are collected and stored.
4. After scraping, the user can choose to send the results via email.

## 📦 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/AdityaKandhare/Web-Scraping-Project.git
   cd Web-Scraping-Project
2. Install required libraries:
pip install -r requirements.txt

3. Run the script:
python scraper.py

📧 Emailing Results
If you choose "yes" when asked to send an email, you’ll be prompted to enter:

Your Gmail credentials (username and app password)
Recipient's email address
The script will then send a simple plain-text email with all scraped book details.



🙋‍♂️ Author
Aditya Kandhare
GitHub


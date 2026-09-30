# Job Listings Web Scraper

A beginner-friendly Python web scraping project that extracts structured job listing information from an HTML webpage and performs basic job and skill analysis.

## Project Overview

This project uses **BeautifulSoup** to parse HTML job listings and **Pandas** to organize the extracted information into a structured dataset.

The project extracts:

- Job title
- Company
- Location
- Skills
- Job link

It also performs basic analysis such as:

- Total number of jobs
- Number of remote jobs
- Number of unique locations
- Skill frequency

> **Note:** The job listings used in this project are fictional practice data created in a local HTML file for learning purposes. They are not scraped from real company websites.

## Technologies Used

- Python
- BeautifulSoup
- Pandas
- HTML
- Git & GitHub

## Project Structure

```text
Job Listings Web Scraper/
├── job_listings.html
├── job_scraper.py
├── jobs.csv
├── scraper.py
├── books.csv
├── requirements.txt
├── .gitignore
└── README.md
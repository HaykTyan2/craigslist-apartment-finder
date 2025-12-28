## apartment-finder-scraper

A Python-based apartment listing scraper that collects rental listings from Craigslist using browser automation and optional scheduled execution.

This project was built as a learning exercise to understand browser-based scraping, form interaction, page traversal, data persistence with SQLite, and task scheduling.

------------------------------------------------------------

## What this project does

The program navigates Craigslist similarly to how a real user would browse the site.

It allows the user to:

• Select a location or ZIP code
• Apply filters such as price range, bedrooms, and amenities
• Browse apartment listings
• Open individual listings
• Extract listing details (title, address, description, notes)
• Save results into a SQLite database
• Optionally run the scraper on a schedule using a Windows batch script

All scraping is done using a real browser session via Playwright.

------------------------------------------------------------

## How it works (high level)

1. A browser session is started using Playwright.
2. Craigslist is opened with a predefined search URL.
3. The location selector is automated (ZIP code or city).
4. Search filters are applied through the left-side panel.
5. Apartment listings are collected from the results page.
6. Each listing is opened in a new browser tab.
7. Listing details are extracted with timeout handling.
8. Extracted data is stored in a SQLite database.
9. The browser session is closed.
10. (Optional) The process can be repeated automatically using a scheduler.

------------------------------------------------------------

## Project structure
```
apartment-finder-scraper/
├── src/
│   ├── browser.py          # Browser lifecycle and page navigation
│   ├── location.py         # Automates Craigslist location selection
│   ├── leftPanel.py        # Collects user filter input
│   ├── leftPanelFiller.py  # Applies filters on the Craigslist UI
│   ├── apt_scraper.py      # Scrapes listing links and opens them
│   ├── apt_scraper2.py     # Extracts details from individual listings
│   ├── database.py         # Handles SQLite database creation and inserts
│
├── apartments.db           # SQLite database (generated at runtime)
├── scheduler.py            # Runs the scraper on a timed interval
├── run_scheduler.bat       # Windows batch file to launch scheduler
├── main.py                 # Entry point and scraping flow controller
├── .gitignore
├── README.md
```
------------------------------------------------------------

File explanations

## main.py  
This is the main entry point of the program.

It is responsible for:
• Initializing the database
• Starting and stopping the browser
• Navigating Craigslist
• Applying filters
• Triggering the scraping process

------------------------------------------------------------

## src/browser.py  
Handles browser automation.

This file:
• Starts the Playwright browser
• Creates browser contexts
• Opens new pages
• Adds polite delays to mimic real user behavior
• Closes browser resources cleanly

Note:
The browser runs in non-headless mode by default for visual debugging.
Users may change `headless=False` to `headless=True` if desired.

------------------------------------------------------------

## src/location.py  
Automates the Craigslist location selector.

This file:
• Opens the location modal
• Types a ZIP code or city
• Selects the first suggested location
• Confirms the location choice

------------------------------------------------------------

## src/leftPanel.py  
Collects filter preferences from the user.

This includes:
• Price range
• Bedroom range
• Optional amenities (pets, furnished, accessibility, etc.)

------------------------------------------------------------

## src/leftPanelFiller.py  
Applies the selected filters directly to Craigslist’s UI.

This file:
• Fills price and bedroom inputs
• Checks applicable filter boxes
• Applies the filters before scraping begins

------------------------------------------------------------

## src/apt_scraper.py  
Handles scraping the listing results page.

This file:
• Locates listing containers
• Extracts listing URLs
• Opens listings in new tabs
• Passes pages to the detailed scraper
• Saves extracted data to the database

------------------------------------------------------------

## src/apt_scraper2.py  
Extracts detailed information from an individual listing.

This includes:
• Listing title
• Street address
• Description
• Notes / attributes
• Listing URL

Timeout handling is used to prevent failures when elements are missing.

------------------------------------------------------------

## src/database.py  
Handles data persistence using SQLite.

This file:
• Creates the listings table if it doesn’t exist
• Inserts scraped listings
• Prevents duplicate entries using a UNIQUE link constraint
• Automatically timestamps each entry

------------------------------------------------------------

## Scheduler and batch file

scheduler.py  
Uses APScheduler to run the scraper at a fixed interval.

This file:
• Runs the scraper automatically (default: every 1 minute)
• Logs activity to a scheduler log file
• Handles errors safely so the scheduler does not crash

------------------------------------------------------------

## run_scheduler.bat  
Windows batch file used to start the scheduler.

Key line:
cd /d "%~dp0"

This line ensures the script always runs from its own directory, making it portable and safe to use on different machines.

The batch file:
• Changes to the project directory automatically
• Launches the Python scheduler
• Keeps the terminal window open for debugging

------------------------------------------------------------

## Installation / Process

Clone the repository:
git clone https://github.com/YOUR_USERNAME/apartment-finder-scraper.git
cd apartment-finder-scraper

Install dependencies:
pip install playwright apscheduler
playwright install

Run the scraper manually:
```
python main.py
```
Run with scheduler (Windows):

Double-click run_scheduler.bat
or
```
python scheduler.py
```

------------------------------------------------------------

## Output

• Apartment listings are saved to a SQLite database (apartments.db)
• Duplicate listings are ignored automatically
• Each run appends new listings if available

------------------------------------------------------------

## Notes and limitations

• This project uses synchronous browser automation.
• It is not optimized for large-scale or high-frequency scraping.
• Craigslist page structure may change over time.
• Scheduler timing can be adjusted in scheduler.py.
• Intended for educational and personal use only.

------------------------------------------------------------

## License

This project is provided for educational use.

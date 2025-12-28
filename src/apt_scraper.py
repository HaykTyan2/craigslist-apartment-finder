from playwright.sync_api import TimeoutError
from src.apt_scraper2 import apt_scraper2
from src.browser import new_page
from src.database import save_listing

def apt_scraper(page):
  container = page.locator("div.results.cl-search-results-pageless.cl-wide")
  page.wait_for_selector("div.cl-search-result[data-pid]", timeout=10000)  # wait up to 10s
  itemDiv = container.locator("div.cl-search-result[data-pid]")
  count = itemDiv.count()
  print("Found:", count)
  limit = min(10, count)
  print(limit)
  print("chekmark")
  for i in range(limit):
    anchor = itemDiv.nth(i).locator("a.cl-app-anchor.cl-search-anchor.text-only[tabindex='0']")
    href = anchor.get_attribute("href")
    print("CHECKMARK2")
    if href:
      newPage = new_page(href.strip())
      individualDict = apt_scraper2(newPage, href.strip())
      save_listing(individualDict)
      newPage.close() # closing each tab after we return from it
      
    

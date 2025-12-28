from playwright.sync_api import sync_playwright
import time, random

_playwright = None
_browser = None
_context = None

def start_browser():
  global _playwright, _browser, _context
  _playwright = sync_playwright().start()
  _browser = _playwright.chromium.launch(headless=False)
  _context = _browser.new_context(
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
              "AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/120.0.0.0 Safari/537.36"
  )

def stop_browser():
  global _playwright, _browser, _context
  if _context:
    _context.close()
  if _browser:
    _browser.close()
  if _playwright:
    _playwright.stop()

def new_page(page):
  global _context
  newPage = _context.new_page()
  
  try:
    #If the page doesn’t load within 30s, Playwright raises an error → your except Exception as e catches it.
    newPage.goto(page, wait_until="domcontentloaded", timeout=30000)

    #picks a random float between 2 and 5
    delay = random.uniform(1.5, 3)

    #pauses the script for that many seconds.
    time.sleep(delay)
    print(f"Polite delay: slept for {delay:.2f} seconds")

    return newPage
  except Exception as e:
    print(f"Failed to load {page}: {e}")
    return None
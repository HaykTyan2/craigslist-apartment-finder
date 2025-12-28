from playwright.sync_api import TimeoutError
import time

def set_location(page, zipcode_or_city: str):
  """
  Automates the Craigslist location selector:
  1. Click the top-left location link
  2. Type city/zip
  3. Choose the first suggestion
  4. Confirm by clicking "choose this location"
  """
# .fill() waits until the input is editable.

# .inner_text() waits until the element exists and is visible.

# .hover() waits until the element is visible and stable.
  try:

    # \d -> means “a digit” (0–9).
    # + -> means “one or more of the previous thing”.
    # even though the text is inside a span which is nested inside the actual button
    # playwright is smart: it will still click the CLOSEST ACTIONABLE ANCESTOR 
    # (in this case the button that it's nested inside of)
    page.locator(r"text=/± \d+ mi/").nth(0).click()

    time.sleep(2)
    # 2. Wait for modal & type into search box
    input_box = page.locator("input[placeholder='city or zip/postal code']")
    input_box.fill("")
    input_box.type(zipcode_or_city, delay=100)

    # 3. Wait for suggestion list and click first suggestion
    suggestion_item = page.locator("div.single-link.highlighted a").first
    suggestion_item.wait_for(state="visible", timeout=5000)
    suggestion_item.click()

    # 4. Click "choose this location"
    time.sleep(6)
    page.locator("button.apply-button:has-text('choose this location')").click()

    return page

  except TimeoutError:
    print("Location selection failed: element not found in time.")

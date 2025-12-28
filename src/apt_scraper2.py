from playwright.sync_api import TimeoutError

def apt_scraper2(page, href: str):
    notesList = []

    try:
        page.wait_for_selector("h1.postingtitle span.postingtitletext", timeout=8000)
        postingTitle = page.locator("h1.postingtitle span.postingtitletext").inner_text().strip()
        print("postingTitle done")
    except TimeoutError:
        postingTitle = "N/A"
        print("postingTitle missing")

    try:
        page.wait_for_selector("h2.street-address", timeout=5000)
        streetAddress = page.locator("h2.street-address").inner_text().strip()
        print("streetAddress done")
    except TimeoutError:
        streetAddress = "N/A"
        print("streetAddress missing")

    try:
        page.wait_for_selector("section[id='postingbody']", timeout=8000)
        description = page.locator("section[id='postingbody']").inner_text().strip()
        print("description done")
    except TimeoutError:
        description = "N/A"
        print("description missing")

    # Wait for notes container too (some listings might not have it)
    try:
        page.wait_for_selector("div.attrgroup", timeout=5000)
        notesContainer = page.locator("div.attrgroup")
        count = notesContainer.count()
        for i in range(count):
            notesList.append(notesContainer.nth(i).inner_text().strip())
        print("notesContainer done")
    except TimeoutError:
        notesList = []
        print("notesContainer missing")

    print("returning..........")
    return {
        "title": postingTitle,
        "address": streetAddress,
        "description": description,
        "link": href,
        "notes": notesList,
    }

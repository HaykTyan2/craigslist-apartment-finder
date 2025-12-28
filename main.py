from src.browser import start_browser, stop_browser, new_page
from src.location import set_location
from src.leftPanel import assigner
from src.leftPanelFiller import fillPanel
from src.apt_scraper import apt_scraper
from src.database import init_db

def main():
  init_db()
  start_browser()
  page = new_page("https://losangeles.craigslist.org/search/littlerock-ca/apa?lat=34.4809&lon=-117.9321&search_distance=60#search=2~gallery~0")

  if page:

    page = set_location(page, "10007")  
    leftPanelOptions = assigner()
    page = fillPanel(page, leftPanelOptions)

    #BEGIN SCRAPING THE APARTMENTS:
    apt_scraper(page)



  stop_browser()


if __name__ == "__main__":
  main()

#RELOAD
#SQLITE and JSON(for practice, using json.dumps(dictList))


# [{
# "title" : postingTitle,
# "address" : streetAddress,
# "description" : description,
# "link": href,
# "notes" : notesList
# }]
# scheduler.py
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import logging
# BlockingScheduler Runs in the main thread and blocks until stopped (good for standalone scripts).
# without BlockingScheduler we wouldnt even have schedular to even do schedular.start() so having BlockingScheduler is basically required and is the first step to always making a scheduler code?
# Think of BlockingScheduler as the blueprint or type of scheduler you want.
#If you use BlockingScheduler, it takes over that main thread and never gives it back — it just loops forever.



# Import your main scraper
from main import main as scrape_main

# --- optional logging so you can check history ---
logging.basicConfig(
    filename="scheduler.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --- the scheduler setup ---
scheduler = BlockingScheduler()

# define the task that runs every 3 minutes
def job():
    logging.info("Starting scrape cycle.")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Running scraper...")

    try:
        scrape_main()
        logging.info("Scrape cycle finished successfully.")
    except Exception as e:
        logging.exception(f"Error during scraping: {e}")

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Waiting for next run...")

# add the job: run every 3 minutes
scheduler.add_job(job, "interval", minutes=1)

# --- start the scheduler ---
if __name__ == "__main__":
    logging.info("Scheduler started.")
    print("Scheduler running — scraping every 3 minutes. Press Ctrl+C to stop.")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logging.info("Scheduler stopped manually.")
        scheduler.shutdown()
        print("Scheduler stopped.")

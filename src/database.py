import sqlite3

# --- connect to database (creates it if not exists) ---
def connect_db():
    conn = sqlite3.connect("apartments.db")
    return conn

# --- create the table if it doesn't exist ---
def init_db():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS listings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            address TEXT,
            description TEXT,
            link TEXT UNIQUE,
            notes TEXT,
            scraped_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit() #save, after this SQLite writes the data changes into the actual DB from the memory
    conn.close() #close so it becomes "unlocked for others to open it" and allows for safer navigation

# --- insert one scraped listing ---
def save_listing(listing: dict):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO listings (title, address, description, link, notes)
        VALUES (:t, :a, :d, :l, :n)
    """, {
        "t": listing.get("title", ""),
        "a": listing.get("address", ""),
        "d": listing.get("description", ""),
        "l": listing.get("link", ""),
        "n": ", ".join(listing.get("notes", []))
    })

    conn.commit()
    conn.close()

# listing = {
#     "title": "Cozy Studio Apartment",
#     "address": "42 Elm Street",
#     "description": "Bright studio with modern kitchen",
#     "link": "https://example.com/listing/42",
#     "notes": ["pet friendly", "balcony"]
# }

def create_users_table(conn):
    """Create users table."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'user'
        )
    """)
    print("Users table created!")
    conn.commit()

def create_cyber_incidents_table(conn):
    """Create the cyber_incidents table."""
    
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS cyber_incidents (
        incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        incident_type TEXT NOT NULL,
        description TEXT,
        date_reported TEXT NOT NULL,
        severity TEXT CHECK(severity IN ('Low', 'Medium', 'High')) NOT NULL,
        FOREIGN KEY (username) REFERENCES users(username)
    );
    """
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()
    print("Cyber incidents table created!")

    conn.commit()

def create_datasets_metadata_table(conn):
    """Create datasets_metadata table."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS datasets_metadata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            created_at TEXT NOT NULL
        )
    """)
    cursor = conn.cursor()
    conn.commit()
    print("Datasets metadata table created!")

def create_it_tickets_table(conn):
    """Create it_tickets table."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS it_tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT
        )
    """)
    cursor = conn.cursor()
    conn.commit()
    print(" IT tickets table created!")

def create_all_tables(conn):
    """Create all tables."""
    create_users_table(conn)
    create_cyber_incidents_table(conn)
    create_datasets_metadata_table(conn)
    create_it_tickets_table(conn)

# Test: Create all tables
from db import connect_database
conn = connect_database()
create_all_tables(conn)
conn.close()


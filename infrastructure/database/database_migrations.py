"""Database schema migrations."""
from infrastructure.database.sqlite_connection import SQLiteConnection


class DatabaseMigrations:
    """Handles database schema creation and migrations."""

    def __init__(self, connection: SQLiteConnection):
        """Initialize migrations.

        Args:
            connection: SQLite connection manager
        """
        self.connection = connection

    def create_tables(self) -> None:
        """Create all database tables if they don't exist."""
        self._create_users_table()
        self._create_employees_table()
        self._create_appointments_table()
        self._create_services_table()

    def _create_users_table(self) -> None:
        """Create users table."""
        query = """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        with self.connection.get_cursor() as cursor:
            cursor.execute(query)

    def _create_employees_table(self) -> None:
        """Create employees table."""
        query = """
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            position TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        with self.connection.get_cursor() as cursor:
            cursor.execute(query)

    def _create_appointments_table(self) -> None:
        """Create appointments table."""
        query = """
        CREATE TABLE IF NOT EXISTS appointments (
            appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            service_name TEXT NOT NULL,
            service_price REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(date, time)
        )
        """
        with self.connection.get_cursor() as cursor:
            cursor.execute(query)

    def _create_services_table(self) -> None:
        """Create services table."""
        query = """
        CREATE TABLE IF NOT EXISTS services (
            service_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            price REAL NOT NULL
        )
        """
        with self.connection.get_cursor() as cursor:
            cursor.execute(query)

    def seed_services(self) -> None:
        """Seed initial services data."""
        services = [
            ("Eyelashes", 25.0),
            ("Manicure", 20.0),
            ("Physiotherapy", 35.0),
            ("Massage", 30.0),
            ("Facial Care", 28.0),
            ("Body Care", 32.0),
            ("Depilation", 15.0),
            ("Laser Depilation", 50.0),
        ]

        # Check if services already exist
        with self.connection.get_cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM services")
            count = cursor.fetchone()[0]

            if count == 0:
                # Insert services
                query = "INSERT INTO services (name, price) VALUES (?, ?)"
                cursor.executemany(query, services)

    def drop_all_tables(self) -> None:
        """Drop all tables (use with caution!)."""
        tables = ["users", "employees", "appointments", "services"]
        with self.connection.get_cursor() as cursor:
            for table in tables:
                cursor.execute(f"DROP TABLE IF EXISTS {table}")

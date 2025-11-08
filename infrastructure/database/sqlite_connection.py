"""SQLite database connection manager."""
import sqlite3
from pathlib import Path
from typing import Optional
from contextlib import contextmanager


class SQLiteConnection:
    """SQLite database connection manager with connection pooling."""

    def __init__(self, database_path: Path):
        """Initialize connection manager.

        Args:
            database_path: Path to SQLite database file
        """
        self.database_path = database_path
        self._connection: Optional[sqlite3.Connection] = None

    def connect(self) -> sqlite3.Connection:
        """Get or create database connection.

        Returns:
            SQLite connection
        """
        if self._connection is None:
            self._connection = sqlite3.connect(
                self.database_path,
                check_same_thread=False
            )
            self._connection.row_factory = sqlite3.Row
        return self._connection

    def close(self) -> None:
        """Close database connection."""
        if self._connection:
            self._connection.close()
            self._connection = None

    @contextmanager
    def get_cursor(self):
        """Context manager for database cursor.

        Yields:
            SQLite cursor

        Example:
            with connection.get_cursor() as cursor:
                cursor.execute("SELECT * FROM users")
        """
        conn = self.connect()
        cursor = conn.cursor()
        try:
            yield cursor
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()

    def execute(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        """Execute a query and return cursor.

        Args:
            query: SQL query to execute
            params: Query parameters

        Returns:
            SQLite cursor
        """
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
            return cursor

    def execute_many(self, query: str, params_list: list) -> None:
        """Execute query multiple times with different parameters.

        Args:
            query: SQL query to execute
            params_list: List of parameter tuples
        """
        with self.get_cursor() as cursor:
            cursor.executemany(query, params_list)

    def fetch_one(self, query: str, params: tuple = ()) -> Optional[sqlite3.Row]:
        """Execute query and fetch one result.

        Args:
            query: SQL query to execute
            params: Query parameters

        Returns:
            Single row or None
        """
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchone()

    def fetch_all(self, query: str, params: tuple = ()) -> list:
        """Execute query and fetch all results.

        Args:
            query: SQL query to execute
            params: Query parameters

        Returns:
            List of rows
        """
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

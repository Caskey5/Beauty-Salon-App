"""SQLite implementation of UserRepository."""
from typing import List, Optional
from core.entities import User
from core.repositories import UserRepository
from infrastructure.database import SQLiteConnection


class SQLiteUserRepository(UserRepository):
    """SQLite implementation of user repository."""

    def __init__(self, connection: SQLiteConnection):
        """Initialize repository.

        Args:
            connection: SQLite connection manager
        """
        self.connection = connection

    def create(self, user: User) -> User:
        """Create a new user."""
        if self.username_exists(user.username):
            raise ValueError(f"Username '{user.username}' already exists")

        query = """
        INSERT INTO users (first_name, last_name, phone_number, username, password_hash)
        VALUES (?, ?, ?, ?, ?)
        """
        with self.connection.get_cursor() as cursor:
            cursor.execute(
                query,
                (
                    user.first_name,
                    user.last_name,
                    user.phone_number,
                    user.username,
                    user.password_hash,
                ),
            )
            user.user_id = cursor.lastrowid
        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID."""
        query = "SELECT * FROM users WHERE user_id = ?"
        row = self.connection.fetch_one(query, (user_id,))

        if row:
            return User(
                user_id=row["user_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                phone_number=row["phone_number"],
                username=row["username"],
                password_hash=row["password_hash"],
            )
        return None

    def get_by_username(self, username: str) -> Optional[User]:
        """Get user by username."""
        query = "SELECT * FROM users WHERE username = ?"
        row = self.connection.fetch_one(query, (username,))

        if row:
            return User(
                user_id=row["user_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                phone_number=row["phone_number"],
                username=row["username"],
                password_hash=row["password_hash"],
            )
        return None

    def get_all(self) -> List[User]:
        """Get all users."""
        query = "SELECT * FROM users ORDER BY user_id"
        rows = self.connection.fetch_all(query)

        return [
            User(
                user_id=row["user_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                phone_number=row["phone_number"],
                username=row["username"],
                password_hash=row["password_hash"],
            )
            for row in rows
        ]

    def update(self, user: User) -> User:
        """Update user."""
        if not user.user_id:
            raise ValueError("User ID is required for update")

        query = """
        UPDATE users
        SET first_name = ?, last_name = ?, phone_number = ?, username = ?, password_hash = ?
        WHERE user_id = ?
        """
        with self.connection.get_cursor() as cursor:
            cursor.execute(
                query,
                (
                    user.first_name,
                    user.last_name,
                    user.phone_number,
                    user.username,
                    user.password_hash,
                    user.user_id,
                ),
            )
            if cursor.rowcount == 0:
                raise ValueError(f"User with ID {user.user_id} not found")

        return user

    def delete(self, user_id: int) -> bool:
        """Delete user."""
        query = "DELETE FROM users WHERE user_id = ?"
        with self.connection.get_cursor() as cursor:
            cursor.execute(query, (user_id,))
            return cursor.rowcount > 0

    def username_exists(self, username: str) -> bool:
        """Check if username exists."""
        query = "SELECT COUNT(*) FROM users WHERE username = ?"
        row = self.connection.fetch_one(query, (username,))
        return row[0] > 0 if row else False

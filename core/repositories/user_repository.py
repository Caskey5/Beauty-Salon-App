"""User repository interface."""
from abc import ABC, abstractmethod
from typing import List, Optional
from core.entities import User


class UserRepository(ABC):
    """Abstract base class for user data access."""

    @abstractmethod
    def create(self, user: User) -> User:
        """Create a new user.

        Args:
            user: User entity to create

        Returns:
            Created user with assigned ID

        Raises:
            ValueError: If username already exists
        """
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID.

        Args:
            user_id: User ID

        Returns:
            User if found, None otherwise
        """
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> Optional[User]:
        """Get user by username.

        Args:
            username: Username to search for

        Returns:
            User if found, None otherwise
        """
        pass

    @abstractmethod
    def get_all(self) -> List[User]:
        """Get all users.

        Returns:
            List of all users
        """
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        """Update user.

        Args:
            user: User entity to update

        Returns:
            Updated user

        Raises:
            ValueError: If user not found
        """
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        """Delete user.

        Args:
            user_id: User ID to delete

        Returns:
            True if deleted, False if not found
        """
        pass

    @abstractmethod
    def username_exists(self, username: str) -> bool:
        """Check if username exists.

        Args:
            username: Username to check

        Returns:
            True if exists, False otherwise
        """
        pass

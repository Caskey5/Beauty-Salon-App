"""User entity - represents a customer of the beauty salon."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    """Customer/User entity.

    Represents a customer who can book appointments.
    """

    first_name: str
    last_name: str
    phone_number: str
    username: str
    password_hash: str
    user_id: Optional[int] = None

    @property
    def full_name(self) -> str:
        """Get user's full name."""
        return f"{self.first_name} {self.last_name}"

    def to_dict(self) -> dict:
        """Convert entity to dictionary."""
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "username": self.username,
            "password_hash": self.password_hash,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """Create entity from dictionary."""
        return cls(
            user_id=data.get("user_id"),
            first_name=data["first_name"],
            last_name=data["last_name"],
            phone_number=data["phone_number"],
            username=data["username"],
            password_hash=data["password_hash"],
        )

    def __str__(self) -> str:
        """String representation."""
        return f"User({self.username}, {self.full_name})"

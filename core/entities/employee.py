"""Employee entity - represents a salon staff member."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Employee:
    """Employee entity.

    Represents a salon staff member who can book appointments for customers.
    """

    first_name: str
    last_name: str
    position: str
    phone_number: str
    username: str
    password_hash: str
    employee_id: Optional[int] = None

    @property
    def full_name(self) -> str:
        """Get employee's full name."""
        return f"{self.first_name} {self.last_name}"

    def to_dict(self) -> dict:
        """Convert entity to dictionary."""
        return {
            "employee_id": self.employee_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "position": self.position,
            "phone_number": self.phone_number,
            "username": self.username,
            "password_hash": self.password_hash,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Employee":
        """Create entity from dictionary."""
        return cls(
            employee_id=data.get("employee_id"),
            first_name=data["first_name"],
            last_name=data["last_name"],
            position=data["position"],
            phone_number=data["phone_number"],
            username=data["username"],
            password_hash=data["password_hash"],
        )

    def __str__(self) -> str:
        """String representation."""
        return f"Employee({self.username}, {self.full_name}, {self.position})"

"""Service entity - represents a beauty salon service."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Service:
    """Service entity.

    Represents a beauty salon service with its pricing.
    """

    name: str
    price: float
    service_id: Optional[int] = None

    @property
    def formatted_price(self) -> str:
        """Get formatted price string."""
        return f"{self.price}€"

    @property
    def display_name(self) -> str:
        """Get display name with price."""
        return f"{self.name} -> {self.formatted_price}"

    def to_dict(self) -> dict:
        """Convert entity to dictionary."""
        return {
            "service_id": self.service_id,
            "name": self.name,
            "price": self.price,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Service":
        """Create entity from dictionary."""
        return cls(
            service_id=data.get("service_id"),
            name=data["name"],
            price=float(data["price"]),
        )

    def __str__(self) -> str:
        """String representation."""
        return f"Service({self.name}, {self.formatted_price})"

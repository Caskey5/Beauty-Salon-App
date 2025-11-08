"""Appointment entity - represents a booked salon appointment."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Appointment:
    """Appointment entity.

    Represents a scheduled appointment for a beauty salon service.
    """

    first_name: str
    last_name: str
    phone_number: str
    date: str  # Format: YYYY-MM-DD
    time: str  # Format: HH:MM
    service_name: str
    service_price: float
    appointment_id: Optional[int] = None

    @property
    def full_name(self) -> str:
        """Get customer's full name."""
        return f"{self.first_name} {self.last_name}"

    @property
    def datetime_str(self) -> str:
        """Get formatted date and time."""
        return f"{self.date} at {self.time}"

    def to_dict(self) -> dict:
        """Convert entity to dictionary."""
        return {
            "appointment_id": self.appointment_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "date": self.date,
            "time": self.time,
            "service_name": self.service_name,
            "service_price": self.service_price,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Appointment":
        """Create entity from dictionary."""
        return cls(
            appointment_id=data.get("appointment_id"),
            first_name=data["first_name"],
            last_name=data["last_name"],
            phone_number=data["phone_number"],
            date=data["date"],
            time=data["time"],
            service_name=data["service_name"],
            service_price=float(data["service_price"]),
        )

    def __str__(self) -> str:
        """String representation."""
        return f"Appointment({self.full_name}, {self.date} {self.time}, {self.service_name})"

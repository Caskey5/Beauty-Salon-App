"""Appointment repository interface."""
from abc import ABC, abstractmethod
from typing import List, Optional
from core.entities import Appointment


class AppointmentRepository(ABC):
    """Abstract base class for appointment data access."""

    @abstractmethod
    def create(self, appointment: Appointment) -> Appointment:
        """Create a new appointment.

        Args:
            appointment: Appointment entity to create

        Returns:
            Created appointment with assigned ID
        """
        pass

    @abstractmethod
    def get_by_id(self, appointment_id: int) -> Optional[Appointment]:
        """Get appointment by ID.

        Args:
            appointment_id: Appointment ID

        Returns:
            Appointment if found, None otherwise
        """
        pass

    @abstractmethod
    def get_all(self) -> List[Appointment]:
        """Get all appointments.

        Returns:
            List of all appointments
        """
        pass

    @abstractmethod
    def get_by_customer(
        self, first_name: str, last_name: str, phone_number: str
    ) -> List[Appointment]:
        """Get appointments by customer details.

        Args:
            first_name: Customer's first name
            last_name: Customer's last name
            phone_number: Customer's phone number

        Returns:
            List of appointments for the customer
        """
        pass

    @abstractmethod
    def get_by_date(self, date: str) -> List[Appointment]:
        """Get appointments by date.

        Args:
            date: Date in YYYY-MM-DD format

        Returns:
            List of appointments on the specified date
        """
        pass

    @abstractmethod
    def get_by_date_and_time(self, date: str, time: str) -> Optional[Appointment]:
        """Get appointment by date and time.

        Args:
            date: Date in YYYY-MM-DD format
            time: Time in HH:MM format

        Returns:
            Appointment if found, None otherwise
        """
        pass

    @abstractmethod
    def update(self, appointment: Appointment) -> Appointment:
        """Update appointment.

        Args:
            appointment: Appointment entity to update

        Returns:
            Updated appointment

        Raises:
            ValueError: If appointment not found
        """
        pass

    @abstractmethod
    def delete(self, appointment_id: int) -> bool:
        """Delete appointment.

        Args:
            appointment_id: Appointment ID to delete

        Returns:
            True if deleted, False if not found
        """
        pass

    @abstractmethod
    def is_time_slot_available(self, date: str, time: str) -> bool:
        """Check if time slot is available.

        Args:
            date: Date in YYYY-MM-DD format
            time: Time in HH:MM format

        Returns:
            True if available, False if booked
        """
        pass

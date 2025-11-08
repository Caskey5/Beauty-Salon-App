"""Get appointments use case."""
from typing import List, Optional

from core.entities import Appointment, User, Employee
from core.repositories import AppointmentRepository
from config.constants import UserRole


class GetAppointments:
    """Use case for retrieving appointments."""

    def __init__(self, appointment_repository: AppointmentRepository):
        """Initialize use case.

        Args:
            appointment_repository: Appointment repository
        """
        self.appointment_repository = appointment_repository

    def get_all(self) -> List[Appointment]:
        """Get all appointments.

        Returns:
            List of all appointments
        """
        return self.appointment_repository.get_all()

    def get_by_customer(
        self, first_name: str, last_name: str, phone_number: str
    ) -> List[Appointment]:
        """Get appointments for specific customer.

        Args:
            first_name: Customer's first name
            last_name: Customer's last name
            phone_number: Customer's phone number

        Returns:
            List of customer's appointments
        """
        return self.appointment_repository.get_by_customer(
            first_name, last_name, phone_number
        )

    def get_by_date(self, date: str) -> List[Appointment]:
        """Get appointments for specific date.

        Args:
            date: Date in YYYY-MM-DD format

        Returns:
            List of appointments on specified date
        """
        return self.appointment_repository.get_by_date(date)

    def get_for_user(
        self, role: UserRole, user: Optional[User] = None, employee: Optional[Employee] = None
    ) -> List[Appointment]:
        """Get appointments based on user role.

        Args:
            role: User role
            user: User entity (for customers)
            employee: Employee entity (for employees)

        Returns:
            List of appointments visible to the user
        """
        if role == UserRole.ADMIN or role == UserRole.EMPLOYEE:
            # Admin and employees can see all appointments
            return self.get_all()
        elif role == UserRole.CUSTOMER and user:
            # Customers can only see their own appointments
            return self.get_by_customer(
                user.first_name, user.last_name, user.phone_number
            )
        else:
            return []

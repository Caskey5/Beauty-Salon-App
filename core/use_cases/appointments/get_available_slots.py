"""Get available time slots use case."""
from typing import List

from core.repositories import AppointmentRepository
from infrastructure.scheduling import WorkingHoursService


class GetAvailableSlots:
    """Use case for getting available time slots."""

    def __init__(
        self,
        appointment_repository: AppointmentRepository,
        working_hours_service: WorkingHoursService,
    ):
        """Initialize use case.

        Args:
            appointment_repository: Appointment repository
            working_hours_service: Working hours service
        """
        self.appointment_repository = appointment_repository
        self.working_hours_service = working_hours_service

    def execute(self, date: str) -> List[str]:
        """Get available time slots for a specific date.

        Args:
            date: Date in YYYY-MM-DD format

        Returns:
            List of available time slots (e.g., ["08:00", "09:00", ...])
        """
        # Get all working hours for the date
        all_hours = self.working_hours_service.get_available_hours(date)

        # Get booked appointments for the date
        booked_appointments = self.appointment_repository.get_by_date(date)
        booked_times = {appointment.time for appointment in booked_appointments}

        # Filter out booked times
        available_slots = [hour for hour in all_hours if hour not in booked_times]

        return available_slots

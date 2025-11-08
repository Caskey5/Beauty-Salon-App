"""Create appointment use case."""
from dataclasses import dataclass
from typing import Optional

from core.entities import Appointment
from core.repositories import AppointmentRepository
from infrastructure.scheduling import WorkingHoursService


@dataclass
class CreateAppointmentResult:
    """Result of create appointment operation."""

    success: bool
    appointment: Optional[Appointment] = None
    message: str = ""


class CreateAppointment:
    """Use case for creating appointments."""

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

    def execute(
        self,
        first_name: str,
        last_name: str,
        phone_number: str,
        date: str,
        time: str,
        service_name: str,
        service_price: float,
    ) -> CreateAppointmentResult:
        """Execute appointment creation.

        Args:
            first_name: Customer's first name
            last_name: Customer's last name
            phone_number: Customer's phone number
            date: Appointment date (YYYY-MM-DD)
            time: Appointment time (HH:MM)
            service_name: Service name
            service_price: Service price

        Returns:
            CreateAppointmentResult with appointment details
        """
        # Validate required fields
        if not all([first_name, last_name, phone_number, date, time, service_name]):
            return CreateAppointmentResult(
                success=False, message="All fields are required"
            )

        # Check if date is a working day
        if not self.working_hours_service.is_working_day(date):
            return CreateAppointmentResult(
                success=False, message="Salon is closed on selected date"
            )

        # Check if time is within working hours
        available_hours = self.working_hours_service.get_available_hours(date)
        if time not in available_hours:
            return CreateAppointmentResult(
                success=False, message="Selected time is outside working hours"
            )

        # Check if time slot is available
        if not self.appointment_repository.is_time_slot_available(date, time):
            return CreateAppointmentResult(
                success=False, message="Time slot is already booked"
            )

        # Create appointment
        appointment = Appointment(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            date=date,
            time=time,
            service_name=service_name,
            service_price=service_price,
        )

        try:
            created_appointment = self.appointment_repository.create(appointment)
            return CreateAppointmentResult(
                success=True,
                appointment=created_appointment,
                message="Appointment created successfully",
            )
        except Exception as e:
            return CreateAppointmentResult(
                success=False, message=f"Failed to create appointment: {str(e)}"
            )

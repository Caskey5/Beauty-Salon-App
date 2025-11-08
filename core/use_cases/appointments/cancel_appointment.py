"""Cancel appointment use case."""
from dataclasses import dataclass

from core.repositories import AppointmentRepository


@dataclass
class CancelAppointmentResult:
    """Result of cancel appointment operation."""

    success: bool
    message: str = ""


class CancelAppointment:
    """Use case for cancelling appointments."""

    def __init__(self, appointment_repository: AppointmentRepository):
        """Initialize use case.

        Args:
            appointment_repository: Appointment repository
        """
        self.appointment_repository = appointment_repository

    def execute(self, appointment_id: int) -> CancelAppointmentResult:
        """Execute appointment cancellation.

        Args:
            appointment_id: ID of appointment to cancel

        Returns:
            CancelAppointmentResult with cancellation status
        """
        try:
            deleted = self.appointment_repository.delete(appointment_id)

            if deleted:
                return CancelAppointmentResult(
                    success=True, message="Appointment cancelled successfully"
                )
            else:
                return CancelAppointmentResult(
                    success=False, message="Appointment not found"
                )
        except Exception as e:
            return CancelAppointmentResult(
                success=False, message=f"Failed to cancel appointment: {str(e)}"
            )

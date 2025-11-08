"""Repository interfaces (abstract base classes)."""
from .user_repository import UserRepository
from .employee_repository import EmployeeRepository
from .appointment_repository import AppointmentRepository
from .service_repository import ServiceRepository

__all__ = [
    "UserRepository",
    "EmployeeRepository",
    "AppointmentRepository",
    "ServiceRepository",
]

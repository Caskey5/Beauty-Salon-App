"""Business constants for Beauty Salon application."""
from enum import Enum
from typing import Dict, List


class UserRole(Enum):
    """User role enumeration."""
    ADMIN = "admin"
    EMPLOYEE = "employee"
    CUSTOMER = "customer"


class EmployeePosition(Enum):
    """Employee position/specialization enumeration."""
    PEDICURIST = "Pedicurist"
    PHYSIOTHERAPIST = "Physiotherapist"
    FACIAL_BODY_CARE = "Facial/Body Care"
    DEPILATION_LASER = "Depilation/Laser"
    MANICURIST = "Manicurist"


class WorkingHours:
    """Working hours configuration."""

    # Monday to Friday
    WEEKDAY_START = "08:00"
    WEEKDAY_END = "21:00"

    # Saturday
    SATURDAY_START = "08:00"
    SATURDAY_END = "13:00"

    # Sunday - closed
    SUNDAY_CLOSED = True

    # Hour interval (in hours)
    HOUR_INTERVAL = 1

    @staticmethod
    def get_weekday_hours() -> List[str]:
        """Get available hours for weekdays (Monday-Friday)."""
        return [f"{hour:02d}:00" for hour in range(8, 21)]

    @staticmethod
    def get_saturday_hours() -> List[str]:
        """Get available hours for Saturday."""
        return [f"{hour:02d}:00" for hour in range(8, 13)]

    @staticmethod
    def get_sunday_hours() -> List[str]:
        """Get available hours for Sunday (closed)."""
        return []


class PasswordRequirements:
    """Password validation requirements."""

    MIN_LENGTH = 8
    REQUIRE_UPPERCASE = True
    REQUIRE_DIGIT = True
    REQUIRE_SPECIAL_CHAR = True
    SPECIAL_CHARS = r'!@#$%^&*(),.?":{}|<>'


class DateFormats:
    """Date format constants."""

    DISPLAY_FORMAT = "%d-%m-%Y"  # DD-MM-YYYY
    STORAGE_FORMAT = "%Y-%m-%d"  # YYYY-MM-DD (ISO format)
    TIME_FORMAT = "%H:%M"        # HH:MM


class Messages:
    """User-facing messages."""

    # Success messages
    LOGIN_SUCCESS = "Login successful!"
    REGISTRATION_SUCCESS = "Registration successful!"
    APPOINTMENT_CREATED = "Appointment created successfully!"
    APPOINTMENT_CANCELLED = "Appointment cancelled successfully!"
    EMPLOYEE_ADDED = "Employee added successfully!"
    EMPLOYEE_REMOVED = "Employee removed successfully!"

    # Error messages
    LOGIN_FAILED = "Invalid username or password!"
    REGISTRATION_FAILED = "Registration failed. Please try again."
    INVALID_PASSWORD = "Password does not meet requirements!"
    PASSWORDS_MISMATCH = "Passwords do not match!"
    USERNAME_EXISTS = "Username already exists!"
    MISSING_FIELDS = "Please fill in all required fields!"
    INVALID_DATE = "Invalid date selected!"
    NO_AVAILABLE_SLOTS = "No available time slots for selected date!"
    APPOINTMENT_NOT_FOUND = "Appointment not found!"

    # Info messages
    WELCOME_MESSAGE = "Welcome to Beauty Salon!"
    PASSWORD_REQUIREMENTS = (
        "Password must be at least 8 characters long and contain:\n"
        "- At least one uppercase letter\n"
        "- At least one digit\n"
        "- At least one special character (!@#$%^&*(),.?\":{}|<>)"
    )

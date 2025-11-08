"""Working hours calculation service."""
from datetime import datetime
from typing import List
from config.constants import WorkingHours


class WorkingHoursService:
    """Service for calculating available working hours."""

    @staticmethod
    def get_available_hours(date_str: str) -> List[str]:
        """Get available working hours for a specific date.

        Args:
            date_str: Date string in DD-MM-YYYY or YYYY-MM-DD format

        Returns:
            List of available time slots (e.g., ["08:00", "09:00", ...])
        """
        try:
            # Try parsing both formats
            try:
                date = datetime.strptime(date_str, "%d-%m-%Y")
            except ValueError:
                date = datetime.strptime(date_str, "%Y-%m-%d")

            # Get day of week (0 = Monday, 6 = Sunday)
            weekday = date.weekday()

            if weekday < 5:  # Monday to Friday
                return WorkingHours.get_weekday_hours()
            elif weekday == 5:  # Saturday
                return WorkingHours.get_saturday_hours()
            else:  # Sunday
                return WorkingHours.get_sunday_hours()

        except ValueError:
            # Invalid date format
            return []

    @staticmethod
    def is_working_day(date_str: str) -> bool:
        """Check if date is a working day.

        Args:
            date_str: Date string in DD-MM-YYYY or YYYY-MM-DD format

        Returns:
            True if it's a working day, False otherwise
        """
        available_hours = WorkingHoursService.get_available_hours(date_str)
        return len(available_hours) > 0

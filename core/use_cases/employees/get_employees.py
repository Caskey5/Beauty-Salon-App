"""Get employees use case."""
from typing import List

from core.entities import Employee
from core.repositories import EmployeeRepository


class GetEmployees:
    """Use case for retrieving employees."""

    def __init__(self, employee_repository: EmployeeRepository):
        """Initialize use case.

        Args:
            employee_repository: Employee repository
        """
        self.employee_repository = employee_repository

    def get_all(self) -> List[Employee]:
        """Get all employees.

        Returns:
            List of all employees
        """
        return self.employee_repository.get_all()

    def get_by_position(self, position: str) -> List[Employee]:
        """Get employees by position.

        Args:
            position: Position/specialization

        Returns:
            List of employees with specified position
        """
        return self.employee_repository.get_by_position(position)

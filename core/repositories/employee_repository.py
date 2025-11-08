"""Employee repository interface."""
from abc import ABC, abstractmethod
from typing import List, Optional
from core.entities import Employee


class EmployeeRepository(ABC):
    """Abstract base class for employee data access."""

    @abstractmethod
    def create(self, employee: Employee) -> Employee:
        """Create a new employee.

        Args:
            employee: Employee entity to create

        Returns:
            Created employee with assigned ID

        Raises:
            ValueError: If username already exists
        """
        pass

    @abstractmethod
    def get_by_id(self, employee_id: int) -> Optional[Employee]:
        """Get employee by ID.

        Args:
            employee_id: Employee ID

        Returns:
            Employee if found, None otherwise
        """
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> Optional[Employee]:
        """Get employee by username.

        Args:
            username: Username to search for

        Returns:
            Employee if found, None otherwise
        """
        pass

    @abstractmethod
    def get_all(self) -> List[Employee]:
        """Get all employees.

        Returns:
            List of all employees
        """
        pass

    @abstractmethod
    def update(self, employee: Employee) -> Employee:
        """Update employee.

        Args:
            employee: Employee entity to update

        Returns:
            Updated employee

        Raises:
            ValueError: If employee not found
        """
        pass

    @abstractmethod
    def delete(self, employee_id: int) -> bool:
        """Delete employee.

        Args:
            employee_id: Employee ID to delete

        Returns:
            True if deleted, False if not found
        """
        pass

    @abstractmethod
    def username_exists(self, username: str) -> bool:
        """Check if username exists.

        Args:
            username: Username to check

        Returns:
            True if exists, False otherwise
        """
        pass

    @abstractmethod
    def get_by_position(self, position: str) -> List[Employee]:
        """Get employees by position.

        Args:
            position: Position to filter by

        Returns:
            List of employees with specified position
        """
        pass

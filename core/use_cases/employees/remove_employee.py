"""Remove employee use case."""
from dataclasses import dataclass

from core.repositories import EmployeeRepository


@dataclass
class RemoveEmployeeResult:
    """Result of remove employee operation."""

    success: bool
    message: str = ""


class RemoveEmployee:
    """Use case for removing employees."""

    def __init__(self, employee_repository: EmployeeRepository):
        """Initialize use case.

        Args:
            employee_repository: Employee repository
        """
        self.employee_repository = employee_repository

    def execute(self, employee_id: int) -> RemoveEmployeeResult:
        """Execute remove employee.

        Args:
            employee_id: ID of employee to remove

        Returns:
            RemoveEmployeeResult with removal status
        """
        try:
            deleted = self.employee_repository.delete(employee_id)

            if deleted:
                return RemoveEmployeeResult(
                    success=True, message="Employee removed successfully"
                )
            else:
                return RemoveEmployeeResult(
                    success=False, message="Employee not found"
                )
        except Exception as e:
            return RemoveEmployeeResult(
                success=False, message=f"Failed to remove employee: {str(e)}"
            )

"""Add employee use case."""
from dataclasses import dataclass
from typing import Optional

from core.entities import Employee
from core.repositories import EmployeeRepository, UserRepository
from infrastructure.security import PasswordHasher, PasswordValidator


@dataclass
class AddEmployeeResult:
    """Result of add employee operation."""

    success: bool
    employee: Optional[Employee] = None
    message: str = ""


class AddEmployee:
    """Use case for adding employees."""

    def __init__(
        self,
        employee_repository: EmployeeRepository,
        user_repository: UserRepository,
        password_hasher: PasswordHasher,
        password_validator: PasswordValidator,
    ):
        """Initialize use case.

        Args:
            employee_repository: Employee repository
            user_repository: User repository
            password_hasher: Password hashing service
            password_validator: Password validation service
        """
        self.employee_repository = employee_repository
        self.user_repository = user_repository
        self.password_hasher = password_hasher
        self.password_validator = password_validator

    def execute(
        self,
        first_name: str,
        last_name: str,
        position: str,
        phone_number: str,
        username: str,
        password: str,
    ) -> AddEmployeeResult:
        """Execute add employee.

        Args:
            first_name: Employee's first name
            last_name: Employee's last name
            position: Employee's position/specialization
            phone_number: Employee's phone number
            username: Username
            password: Plain text password

        Returns:
            AddEmployeeResult with employee details
        """
        # Validate required fields
        if not all([first_name, last_name, position, phone_number, username, password]):
            return AddEmployeeResult(
                success=False, message="All fields are required"
            )

        # Validate password strength
        if not self.password_validator.is_valid(password):
            return AddEmployeeResult(
                success=False,
                message=self.password_validator.get_validation_message(),
            )

        # Check if username already exists (in both users and employees)
        if self.employee_repository.username_exists(username):
            return AddEmployeeResult(
                success=False, message=f"Username '{username}' already exists"
            )

        if self.user_repository.username_exists(username):
            return AddEmployeeResult(
                success=False, message=f"Username '{username}' already exists"
            )

        # Hash password
        password_hash = self.password_hasher.hash_password(password)

        # Create employee
        employee = Employee(
            first_name=first_name,
            last_name=last_name,
            position=position,
            phone_number=phone_number,
            username=username,
            password_hash=password_hash,
        )

        try:
            created_employee = self.employee_repository.create(employee)
            return AddEmployeeResult(
                success=True,
                employee=created_employee,
                message="Employee added successfully",
            )
        except Exception as e:
            return AddEmployeeResult(
                success=False, message=f"Failed to add employee: {str(e)}"
            )

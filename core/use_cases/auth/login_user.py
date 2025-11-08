"""Login user use case."""
from typing import Optional, Tuple
from dataclasses import dataclass

from core.entities import User, Employee
from core.repositories import UserRepository, EmployeeRepository
from infrastructure.security import PasswordHasher
from config.constants import UserRole
from config.settings import settings


@dataclass
class LoginResult:
    """Result of login operation."""

    success: bool
    role: Optional[UserRole] = None
    user: Optional[User] = None
    employee: Optional[Employee] = None
    message: str = ""


class LoginUser:
    """Use case for user authentication."""

    def __init__(
        self,
        user_repository: UserRepository,
        employee_repository: EmployeeRepository,
        password_hasher: PasswordHasher,
    ):
        """Initialize use case.

        Args:
            user_repository: User repository
            employee_repository: Employee repository
            password_hasher: Password hashing service
        """
        self.user_repository = user_repository
        self.employee_repository = employee_repository
        self.password_hasher = password_hasher

    def execute(self, username: str, password: str) -> LoginResult:
        """Execute login.

        Args:
            username: Username
            password: Plain text password

        Returns:
            LoginResult with authentication details
        """
        # Check if admin (hardcoded credentials)
        if self._check_admin(username, password):
            return LoginResult(
                success=True,
                role=UserRole.ADMIN,
                message="Admin login successful",
            )

        # Check if customer user
        user = self.user_repository.get_by_username(username)
        if user:
            if self.password_hasher.verify_password(password, user.password_hash):
                return LoginResult(
                    success=True,
                    role=UserRole.CUSTOMER,
                    user=user,
                    message="Customer login successful",
                )

        # Check if employee
        employee = self.employee_repository.get_by_username(username)
        if employee:
            if self.password_hasher.verify_password(password, employee.password_hash):
                return LoginResult(
                    success=True,
                    role=UserRole.EMPLOYEE,
                    employee=employee,
                    message="Employee login successful",
                )

        # Login failed
        return LoginResult(
            success=False, message="Invalid username or password"
        )

    def _check_admin(self, username: str, password: str) -> bool:
        """Check if credentials match admin.

        Args:
            username: Username
            password: Password

        Returns:
            True if admin credentials match
        """
        return (
            username == settings.ADMIN_USERNAME
            and password == settings.ADMIN_PASSWORD
        )

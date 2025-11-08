"""Register user use case."""
from dataclasses import dataclass
from typing import Optional

from core.entities import User
from core.repositories import UserRepository, EmployeeRepository
from infrastructure.security import PasswordHasher, PasswordValidator


@dataclass
class RegistrationResult:
    """Result of registration operation."""

    success: bool
    user: Optional[User] = None
    message: str = ""


class RegisterUser:
    """Use case for user registration."""

    def __init__(
        self,
        user_repository: UserRepository,
        employee_repository: EmployeeRepository,
        password_hasher: PasswordHasher,
        password_validator: PasswordValidator,
    ):
        """Initialize use case.

        Args:
            user_repository: User repository
            employee_repository: Employee repository
            password_hasher: Password hashing service
            password_validator: Password validation service
        """
        self.user_repository = user_repository
        self.employee_repository = employee_repository
        self.password_hasher = password_hasher
        self.password_validator = password_validator

    def execute(
        self,
        first_name: str,
        last_name: str,
        phone_number: str,
        username: str,
        password: str,
        password_confirm: str,
    ) -> RegistrationResult:
        """Execute user registration.

        Args:
            first_name: User's first name
            last_name: User's last name
            phone_number: User's phone number
            username: Desired username
            password: Plain text password
            password_confirm: Password confirmation

        Returns:
            RegistrationResult with registration details
        """
        # Validate all fields are filled
        if not all([first_name, last_name, phone_number, username, password, password_confirm]):
            return RegistrationResult(
                success=False, message="All fields are required"
            )

        # Validate passwords match
        if password != password_confirm:
            return RegistrationResult(
                success=False, message="Passwords do not match"
            )

        # Validate password strength
        if not self.password_validator.is_valid(password):
            return RegistrationResult(
                success=False,
                message=self.password_validator.get_validation_message(),
            )

        # Check if username already exists (in both users and employees)
        if self.user_repository.username_exists(username):
            return RegistrationResult(
                success=False, message=f"Username '{username}' already exists"
            )

        if self.employee_repository.username_exists(username):
            return RegistrationResult(
                success=False, message=f"Username '{username}' already exists"
            )

        # Hash password
        password_hash = self.password_hasher.hash_password(password)

        # Create user
        user = User(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            username=username,
            password_hash=password_hash,
        )

        try:
            created_user = self.user_repository.create(user)
            return RegistrationResult(
                success=True,
                user=created_user,
                message="Registration successful",
            )
        except Exception as e:
            return RegistrationResult(
                success=False, message=f"Registration failed: {str(e)}"
            )

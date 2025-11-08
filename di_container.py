"""Dependency Injection Container - wires all dependencies together."""
from pathlib import Path

from config.settings import settings
from infrastructure.database import SQLiteConnection, DatabaseMigrations
from infrastructure.security import PasswordHasher, PasswordValidator
from infrastructure.file_handlers import ReceiptGenerator
from infrastructure.scheduling import WorkingHoursService

from data.repositories.sqlite.sqlite_user_repository import SQLiteUserRepository
from data.repositories.sqlite.sqlite_employee_repository import SQLiteEmployeeRepository
from data.repositories.sqlite.sqlite_appointment_repository import SQLiteAppointmentRepository
from data.repositories.sqlite.sqlite_service_repository import SQLiteServiceRepository

from core.use_cases.auth import LoginUser, RegisterUser
from core.use_cases.appointments import (
    CreateAppointment,
    CancelAppointment,
    GetAppointments,
    GetAvailableSlots,
)
from core.use_cases.employees import AddEmployee, RemoveEmployee, GetEmployees
from core.use_cases.services import GetServices


class DIContainer:
    """Dependency Injection Container.

    Centralized location for creating and managing all application dependencies.
    """

    def __init__(self):
        """Initialize container and all dependencies."""
        # Ensure directories exist
        settings.ensure_directories()

        # Infrastructure
        self._db_connection = None
        self._password_hasher = PasswordHasher()
        self._password_validator = PasswordValidator()
        self._receipt_generator = ReceiptGenerator(settings.RECEIPTS_DIR)
        self._working_hours_service = WorkingHoursService()

        # Repositories
        self._user_repository = None
        self._employee_repository = None
        self._appointment_repository = None
        self._service_repository = None

        # Use cases
        self._login_user = None
        self._register_user = None
        self._create_appointment = None
        self._cancel_appointment = None
        self._get_appointments = None
        self._get_available_slots = None
        self._add_employee = None
        self._remove_employee = None
        self._get_employees = None
        self._get_services = None

    # Infrastructure Properties

    @property
    def db_connection(self) -> SQLiteConnection:
        """Get database connection (singleton)."""
        if self._db_connection is None:
            self._db_connection = SQLiteConnection(settings.DATABASE_PATH)
            # Run migrations
            migrations = DatabaseMigrations(self._db_connection)
            migrations.create_tables()
            migrations.seed_services()
        return self._db_connection

    @property
    def password_hasher(self) -> PasswordHasher:
        """Get password hasher."""
        return self._password_hasher

    @property
    def password_validator(self) -> PasswordValidator:
        """Get password validator."""
        return self._password_validator

    @property
    def receipt_generator(self) -> ReceiptGenerator:
        """Get receipt generator."""
        return self._receipt_generator

    @property
    def working_hours_service(self) -> WorkingHoursService:
        """Get working hours service."""
        return self._working_hours_service

    # Repository Properties

    @property
    def user_repository(self):
        """Get user repository."""
        if self._user_repository is None:
            self._user_repository = SQLiteUserRepository(self.db_connection)
        return self._user_repository

    @property
    def employee_repository(self):
        """Get employee repository."""
        if self._employee_repository is None:
            self._employee_repository = SQLiteEmployeeRepository(self.db_connection)
        return self._employee_repository

    @property
    def appointment_repository(self):
        """Get appointment repository."""
        if self._appointment_repository is None:
            self._appointment_repository = SQLiteAppointmentRepository(self.db_connection)
        return self._appointment_repository

    @property
    def service_repository(self):
        """Get service repository."""
        if self._service_repository is None:
            self._service_repository = SQLiteServiceRepository(self.db_connection)
        return self._service_repository

    # Use Case Properties

    @property
    def login_user(self) -> LoginUser:
        """Get login user use case."""
        if self._login_user is None:
            self._login_user = LoginUser(
                self.user_repository,
                self.employee_repository,
                self.password_hasher,
            )
        return self._login_user

    @property
    def register_user(self) -> RegisterUser:
        """Get register user use case."""
        if self._register_user is None:
            self._register_user = RegisterUser(
                self.user_repository,
                self.employee_repository,
                self.password_hasher,
                self.password_validator,
            )
        return self._register_user

    @property
    def create_appointment(self) -> CreateAppointment:
        """Get create appointment use case."""
        if self._create_appointment is None:
            self._create_appointment = CreateAppointment(
                self.appointment_repository,
                self.working_hours_service,
            )
        return self._create_appointment

    @property
    def cancel_appointment(self) -> CancelAppointment:
        """Get cancel appointment use case."""
        if self._cancel_appointment is None:
            self._cancel_appointment = CancelAppointment(self.appointment_repository)
        return self._cancel_appointment

    @property
    def get_appointments(self) -> GetAppointments:
        """Get appointments use case."""
        if self._get_appointments is None:
            self._get_appointments = GetAppointments(self.appointment_repository)
        return self._get_appointments

    @property
    def get_available_slots(self) -> GetAvailableSlots:
        """Get available slots use case."""
        if self._get_available_slots is None:
            self._get_available_slots = GetAvailableSlots(
                self.appointment_repository,
                self.working_hours_service,
            )
        return self._get_available_slots

    @property
    def add_employee(self) -> AddEmployee:
        """Get add employee use case."""
        if self._add_employee is None:
            self._add_employee = AddEmployee(
                self.employee_repository,
                self.user_repository,
                self.password_hasher,
                self.password_validator,
            )
        return self._add_employee

    @property
    def remove_employee(self) -> RemoveEmployee:
        """Get remove employee use case."""
        if self._remove_employee is None:
            self._remove_employee = RemoveEmployee(self.employee_repository)
        return self._remove_employee

    @property
    def get_employees(self) -> GetEmployees:
        """Get employees use case."""
        if self._get_employees is None:
            self._get_employees = GetEmployees(self.employee_repository)
        return self._get_employees

    @property
    def get_services(self) -> GetServices:
        """Get services use case."""
        if self._get_services is None:
            self._get_services = GetServices(self.service_repository)
        return self._get_services

    def cleanup(self):
        """Cleanup resources."""
        if self._db_connection:
            self._db_connection.close()

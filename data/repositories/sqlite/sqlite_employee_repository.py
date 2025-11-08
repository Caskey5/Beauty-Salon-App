"""SQLite implementation of EmployeeRepository."""
from typing import List, Optional
from core.entities import Employee
from core.repositories import EmployeeRepository
from infrastructure.database import SQLiteConnection


class SQLiteEmployeeRepository(EmployeeRepository):
    """SQLite implementation of employee repository."""

    def __init__(self, connection: SQLiteConnection):
        """Initialize repository.

        Args:
            connection: SQLite connection manager
        """
        self.connection = connection

    def create(self, employee: Employee) -> Employee:
        """Create a new employee."""
        if self.username_exists(employee.username):
            raise ValueError(f"Username '{employee.username}' already exists")

        query = """
        INSERT INTO employees (first_name, last_name, position, phone_number, username, password_hash)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        with self.connection.get_cursor() as cursor:
            cursor.execute(
                query,
                (
                    employee.first_name,
                    employee.last_name,
                    employee.position,
                    employee.phone_number,
                    employee.username,
                    employee.password_hash,
                ),
            )
            employee.employee_id = cursor.lastrowid
        return employee

    def get_by_id(self, employee_id: int) -> Optional[Employee]:
        """Get employee by ID."""
        query = "SELECT * FROM employees WHERE employee_id = ?"
        row = self.connection.fetch_one(query, (employee_id,))

        if row:
            return Employee(
                employee_id=row["employee_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                position=row["position"],
                phone_number=row["phone_number"],
                username=row["username"],
                password_hash=row["password_hash"],
            )
        return None

    def get_by_username(self, username: str) -> Optional[Employee]:
        """Get employee by username."""
        query = "SELECT * FROM employees WHERE username = ?"
        row = self.connection.fetch_one(query, (username,))

        if row:
            return Employee(
                employee_id=row["employee_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                position=row["position"],
                phone_number=row["phone_number"],
                username=row["username"],
                password_hash=row["password_hash"],
            )
        return None

    def get_all(self) -> List[Employee]:
        """Get all employees."""
        query = "SELECT * FROM employees ORDER BY employee_id"
        rows = self.connection.fetch_all(query)

        return [
            Employee(
                employee_id=row["employee_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                position=row["position"],
                phone_number=row["phone_number"],
                username=row["username"],
                password_hash=row["password_hash"],
            )
            for row in rows
        ]

    def update(self, employee: Employee) -> Employee:
        """Update employee."""
        if not employee.employee_id:
            raise ValueError("Employee ID is required for update")

        query = """
        UPDATE employees
        SET first_name = ?, last_name = ?, position = ?, phone_number = ?, username = ?, password_hash = ?
        WHERE employee_id = ?
        """
        with self.connection.get_cursor() as cursor:
            cursor.execute(
                query,
                (
                    employee.first_name,
                    employee.last_name,
                    employee.position,
                    employee.phone_number,
                    employee.username,
                    employee.password_hash,
                    employee.employee_id,
                ),
            )
            if cursor.rowcount == 0:
                raise ValueError(f"Employee with ID {employee.employee_id} not found")

        return employee

    def delete(self, employee_id: int) -> bool:
        """Delete employee."""
        query = "DELETE FROM employees WHERE employee_id = ?"
        with self.connection.get_cursor() as cursor:
            cursor.execute(query, (employee_id,))
            return cursor.rowcount > 0

    def username_exists(self, username: str) -> bool:
        """Check if username exists."""
        query = "SELECT COUNT(*) FROM employees WHERE username = ?"
        row = self.connection.fetch_one(query, (username,))
        return row[0] > 0 if row else False

    def get_by_position(self, position: str) -> List[Employee]:
        """Get employees by position."""
        query = "SELECT * FROM employees WHERE position = ? ORDER BY employee_id"
        rows = self.connection.fetch_all(query, (position,))

        return [
            Employee(
                employee_id=row["employee_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                position=row["position"],
                phone_number=row["phone_number"],
                username=row["username"],
                password_hash=row["password_hash"],
            )
            for row in rows
        ]

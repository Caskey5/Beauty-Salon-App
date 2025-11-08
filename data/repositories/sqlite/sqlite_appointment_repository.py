"""SQLite implementation of AppointmentRepository."""
from typing import List, Optional
from core.entities import Appointment
from core.repositories import AppointmentRepository
from infrastructure.database import SQLiteConnection


class SQLiteAppointmentRepository(AppointmentRepository):
    """SQLite implementation of appointment repository."""

    def __init__(self, connection: SQLiteConnection):
        """Initialize repository.

        Args:
            connection: SQLite connection manager
        """
        self.connection = connection

    def create(self, appointment: Appointment) -> Appointment:
        """Create a new appointment."""
        # Check if time slot is available
        if not self.is_time_slot_available(appointment.date, appointment.time):
            raise ValueError(
                f"Time slot {appointment.date} at {appointment.time} is already booked"
            )

        query = """
        INSERT INTO appointments
        (first_name, last_name, phone_number, date, time, service_name, service_price)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        with self.connection.get_cursor() as cursor:
            cursor.execute(
                query,
                (
                    appointment.first_name,
                    appointment.last_name,
                    appointment.phone_number,
                    appointment.date,
                    appointment.time,
                    appointment.service_name,
                    appointment.service_price,
                ),
            )
            appointment.appointment_id = cursor.lastrowid
        return appointment

    def get_by_id(self, appointment_id: int) -> Optional[Appointment]:
        """Get appointment by ID."""
        query = "SELECT * FROM appointments WHERE appointment_id = ?"
        row = self.connection.fetch_one(query, (appointment_id,))

        if row:
            return Appointment(
                appointment_id=row["appointment_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                phone_number=row["phone_number"],
                date=row["date"],
                time=row["time"],
                service_name=row["service_name"],
                service_price=row["service_price"],
            )
        return None

    def get_all(self) -> List[Appointment]:
        """Get all appointments."""
        query = "SELECT * FROM appointments ORDER BY date, time"
        rows = self.connection.fetch_all(query)

        return [
            Appointment(
                appointment_id=row["appointment_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                phone_number=row["phone_number"],
                date=row["date"],
                time=row["time"],
                service_name=row["service_name"],
                service_price=row["service_price"],
            )
            for row in rows
        ]

    def get_by_customer(
        self, first_name: str, last_name: str, phone_number: str
    ) -> List[Appointment]:
        """Get appointments by customer details."""
        query = """
        SELECT * FROM appointments
        WHERE first_name = ? AND last_name = ? AND phone_number = ?
        ORDER BY date, time
        """
        rows = self.connection.fetch_all(query, (first_name, last_name, phone_number))

        return [
            Appointment(
                appointment_id=row["appointment_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                phone_number=row["phone_number"],
                date=row["date"],
                time=row["time"],
                service_name=row["service_name"],
                service_price=row["service_price"],
            )
            for row in rows
        ]

    def get_by_date(self, date: str) -> List[Appointment]:
        """Get appointments by date."""
        query = "SELECT * FROM appointments WHERE date = ? ORDER BY time"
        rows = self.connection.fetch_all(query, (date,))

        return [
            Appointment(
                appointment_id=row["appointment_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                phone_number=row["phone_number"],
                date=row["date"],
                time=row["time"],
                service_name=row["service_name"],
                service_price=row["service_price"],
            )
            for row in rows
        ]

    def get_by_date_and_time(self, date: str, time: str) -> Optional[Appointment]:
        """Get appointment by date and time."""
        query = "SELECT * FROM appointments WHERE date = ? AND time = ?"
        row = self.connection.fetch_one(query, (date, time))

        if row:
            return Appointment(
                appointment_id=row["appointment_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                phone_number=row["phone_number"],
                date=row["date"],
                time=row["time"],
                service_name=row["service_name"],
                service_price=row["service_price"],
            )
        return None

    def update(self, appointment: Appointment) -> Appointment:
        """Update appointment."""
        if not appointment.appointment_id:
            raise ValueError("Appointment ID is required for update")

        query = """
        UPDATE appointments
        SET first_name = ?, last_name = ?, phone_number = ?,
            date = ?, time = ?, service_name = ?, service_price = ?
        WHERE appointment_id = ?
        """
        with self.connection.get_cursor() as cursor:
            cursor.execute(
                query,
                (
                    appointment.first_name,
                    appointment.last_name,
                    appointment.phone_number,
                    appointment.date,
                    appointment.time,
                    appointment.service_name,
                    appointment.service_price,
                    appointment.appointment_id,
                ),
            )
            if cursor.rowcount == 0:
                raise ValueError(
                    f"Appointment with ID {appointment.appointment_id} not found"
                )

        return appointment

    def delete(self, appointment_id: int) -> bool:
        """Delete appointment."""
        query = "DELETE FROM appointments WHERE appointment_id = ?"
        with self.connection.get_cursor() as cursor:
            cursor.execute(query, (appointment_id,))
            return cursor.rowcount > 0

    def is_time_slot_available(self, date: str, time: str) -> bool:
        """Check if time slot is available."""
        existing = self.get_by_date_and_time(date, time)
        return existing is None

"""SQLite implementation of ServiceRepository."""
from typing import List, Optional
from core.entities import Service
from core.repositories import ServiceRepository
from infrastructure.database import SQLiteConnection


class SQLiteServiceRepository(ServiceRepository):
    """SQLite implementation of service repository."""

    def __init__(self, connection: SQLiteConnection):
        """Initialize repository.

        Args:
            connection: SQLite connection manager
        """
        self.connection = connection

    def create(self, service: Service) -> Service:
        """Create a new service."""
        query = "INSERT INTO services (name, price) VALUES (?, ?)"
        with self.connection.get_cursor() as cursor:
            cursor.execute(query, (service.name, service.price))
            service.service_id = cursor.lastrowid
        return service

    def get_by_id(self, service_id: int) -> Optional[Service]:
        """Get service by ID."""
        query = "SELECT * FROM services WHERE service_id = ?"
        row = self.connection.fetch_one(query, (service_id,))

        if row:
            return Service(
                service_id=row["service_id"],
                name=row["name"],
                price=row["price"],
            )
        return None

    def get_by_name(self, name: str) -> Optional[Service]:
        """Get service by name."""
        query = "SELECT * FROM services WHERE name = ?"
        row = self.connection.fetch_one(query, (name,))

        if row:
            return Service(
                service_id=row["service_id"],
                name=row["name"],
                price=row["price"],
            )
        return None

    def get_all(self) -> List[Service]:
        """Get all services."""
        query = "SELECT * FROM services ORDER BY name"
        rows = self.connection.fetch_all(query)

        return [
            Service(
                service_id=row["service_id"],
                name=row["name"],
                price=row["price"],
            )
            for row in rows
        ]

    def update(self, service: Service) -> Service:
        """Update service."""
        if not service.service_id:
            raise ValueError("Service ID is required for update")

        query = "UPDATE services SET name = ?, price = ? WHERE service_id = ?"
        with self.connection.get_cursor() as cursor:
            cursor.execute(
                query, (service.name, service.price, service.service_id)
            )
            if cursor.rowcount == 0:
                raise ValueError(f"Service with ID {service.service_id} not found")

        return service

    def delete(self, service_id: int) -> bool:
        """Delete service."""
        query = "DELETE FROM services WHERE service_id = ?"
        with self.connection.get_cursor() as cursor:
            cursor.execute(query, (service_id,))
            return cursor.rowcount > 0

"""Service repository interface."""
from abc import ABC, abstractmethod
from typing import List, Optional
from core.entities import Service


class ServiceRepository(ABC):
    """Abstract base class for service data access."""

    @abstractmethod
    def create(self, service: Service) -> Service:
        """Create a new service.

        Args:
            service: Service entity to create

        Returns:
            Created service with assigned ID
        """
        pass

    @abstractmethod
    def get_by_id(self, service_id: int) -> Optional[Service]:
        """Get service by ID.

        Args:
            service_id: Service ID

        Returns:
            Service if found, None otherwise
        """
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Service]:
        """Get service by name.

        Args:
            name: Service name

        Returns:
            Service if found, None otherwise
        """
        pass

    @abstractmethod
    def get_all(self) -> List[Service]:
        """Get all services.

        Returns:
            List of all services
        """
        pass

    @abstractmethod
    def update(self, service: Service) -> Service:
        """Update service.

        Args:
            service: Service entity to update

        Returns:
            Updated service

        Raises:
            ValueError: If service not found
        """
        pass

    @abstractmethod
    def delete(self, service_id: int) -> bool:
        """Delete service.

        Args:
            service_id: Service ID to delete

        Returns:
            True if deleted, False if not found
        """
        pass

"""Get services use case."""
from typing import List

from core.entities import Service
from core.repositories import ServiceRepository


class GetServices:
    """Use case for retrieving services."""

    def __init__(self, service_repository: ServiceRepository):
        """Initialize use case.

        Args:
            service_repository: Service repository
        """
        self.service_repository = service_repository

    def get_all(self) -> List[Service]:
        """Get all services.

        Returns:
            List of all services
        """
        return self.service_repository.get_all()

    def get_display_names(self) -> List[str]:
        """Get service display names (name -> price).

        Returns:
            List of formatted service names with prices
        """
        services = self.get_all()
        return [service.display_name for service in services]

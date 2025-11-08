"""
Beauty Salon Application - Main Entry Point

Clean Architecture Implementation
"""
from di_container import DIContainer
from presentation.application import BeautySalonApplication


def main():
    """Main entry point - initializes DI container and starts application."""
    # Initialize dependency injection container
    container = DIContainer()

    # Create and run application
    app = BeautySalonApplication(container)
    app.run()

    # Cleanup on exit
    container.cleanup()


if __name__ == "__main__":
    main()

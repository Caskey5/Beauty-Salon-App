"""
Beauty Salon Application - Main Entry Point

Clean Architecture Implementation
"""
from di_container import DIContainer
from presentation.application import BeautySalonApplication


def main():
    """Main entry point - initializes DI container and starts application."""
    print("Starting Beauty Salon Application...")

    # Initialize dependency injection container
    print("Initializing DI Container...")
    container = DIContainer()
    print("DI Container initialized!")

    # Create and run application
    print("Creating Application...")
    app = BeautySalonApplication(container)
    print("Application created! Starting main loop...")
    app.run()
    print("Application closed.")

    # Cleanup on exit
    print("Cleaning up...")
    container.cleanup()
    print("Cleanup complete.")


if __name__ == "__main__":
    main()

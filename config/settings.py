"""Application settings and configuration."""
import os
from pathlib import Path


class Settings:
    """Application configuration settings."""

    # Base directory
    BASE_DIR = Path(__file__).parent.parent

    # Data sources
    DATA_DIR = BASE_DIR / "data" / "sources"
    RECEIPTS_DIR = BASE_DIR / "receipts"
    ASSETS_DIR = BASE_DIR / "assets"

    # Database
    DATABASE_PATH = DATA_DIR / "salon.db"
    USE_SQLITE = True  # Set to False to use JSON instead

    # JSON files
    USERS_JSON = DATA_DIR / "users.json"
    EMPLOYEES_JSON = DATA_DIR / "employees.json"
    APPOINTMENTS_JSON = DATA_DIR / "appointments.json"
    SERVICES_JSON = DATA_DIR / "services.json"

    # UI Settings
    WINDOW_TITLE = "Beauty Salon"
    WINDOW_WIDTH = 700
    WINDOW_HEIGHT = 550
    BACKGROUND_IMAGE = ASSETS_DIR / "images" / "background.png"
    BACKGROUND_COLOR = "light salmon"

    # Admin credentials (hardcoded)
    ADMIN_USERNAME = "Caskey"
    ADMIN_PASSWORD = "#Caskey123"

    # Ensure directories exist
    @classmethod
    def ensure_directories(cls):
        """Create necessary directories if they don't exist."""
        cls.DATA_DIR.mkdir(parents=True, exist_ok=True)
        cls.RECEIPTS_DIR.mkdir(parents=True, exist_ok=True)
        (cls.ASSETS_DIR / "images").mkdir(parents=True, exist_ok=True)


# Create singleton instance
settings = Settings()

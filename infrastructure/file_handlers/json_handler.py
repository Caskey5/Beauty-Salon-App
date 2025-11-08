"""JSON file handler for reading and writing JSON data."""
import json
from pathlib import Path
from typing import Any, List, Dict


class JsonHandler:
    """Handles JSON file operations."""

    @staticmethod
    def read(file_path: Path) -> List[Dict[str, Any]]:
        """Read data from JSON file.

        Args:
            file_path: Path to JSON file

        Returns:
            List of dictionaries from JSON file
        """
        if not file_path.exists():
            return []

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, IOError):
            return []

    @staticmethod
    def write(file_path: Path, data: List[Dict[str, Any]]) -> None:
        """Write data to JSON file.

        Args:
            file_path: Path to JSON file
            data: List of dictionaries to write
        """
        # Ensure parent directory exists
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @staticmethod
    def append(file_path: Path, item: Dict[str, Any]) -> None:
        """Append item to JSON file.

        Args:
            file_path: Path to JSON file
            item: Dictionary to append
        """
        data = JsonHandler.read(file_path)
        data.append(item)
        JsonHandler.write(file_path, data)

    @staticmethod
    def update_item(
        file_path: Path,
        predicate: callable,
        updated_item: Dict[str, Any]
    ) -> bool:
        """Update item in JSON file.

        Args:
            file_path: Path to JSON file
            predicate: Function to find item to update
            updated_item: Updated item dictionary

        Returns:
            True if item was found and updated, False otherwise
        """
        data = JsonHandler.read(file_path)
        for i, item in enumerate(data):
            if predicate(item):
                data[i] = updated_item
                JsonHandler.write(file_path, data)
                return True
        return False

    @staticmethod
    def delete_item(file_path: Path, predicate: callable) -> bool:
        """Delete item from JSON file.

        Args:
            file_path: Path to JSON file
            predicate: Function to find item to delete

        Returns:
            True if item was found and deleted, False otherwise
        """
        data = JsonHandler.read(file_path)
        original_length = len(data)
        data = [item for item in data if not predicate(item)]

        if len(data) < original_length:
            JsonHandler.write(file_path, data)
            return True
        return False

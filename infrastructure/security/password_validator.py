"""Password validation service."""
import re
from config.constants import PasswordRequirements


class PasswordValidator:
    """Password validation service.

    Validates passwords against security requirements.
    """

    @staticmethod
    def is_valid(password: str) -> bool:
        """Validate password against requirements.

        Args:
            password: Password to validate

        Returns:
            True if password meets all requirements, False otherwise
        """
        # Check minimum length
        if len(password) < PasswordRequirements.MIN_LENGTH:
            return False

        # Check for uppercase letter
        if PasswordRequirements.REQUIRE_UPPERCASE:
            if not re.search(r"[A-Z]", password):
                return False

        # Check for digit
        if PasswordRequirements.REQUIRE_DIGIT:
            if not re.search(r"\d", password):
                return False

        # Check for special character
        if PasswordRequirements.REQUIRE_SPECIAL_CHAR:
            special_chars = re.escape(PasswordRequirements.SPECIAL_CHARS)
            if not re.search(f"[{special_chars}]", password):
                return False

        return True

    @staticmethod
    def get_validation_message() -> str:
        """Get password validation requirements message.

        Returns:
            User-friendly message describing password requirements
        """
        from config.constants import Messages
        return Messages.PASSWORD_REQUIREMENTS

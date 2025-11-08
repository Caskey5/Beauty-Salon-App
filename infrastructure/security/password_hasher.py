"""Password hashing service using SHA-256."""
import hashlib


class PasswordHasher:
    """Password hashing service.

    Uses SHA-256 for password hashing.
    """

    @staticmethod
    def hash_password(password: str) -> str:
        """Hash a password using SHA-256.

        Args:
            password: Plain text password

        Returns:
            Hashed password as hex string
        """
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(password: str, password_hash: str) -> bool:
        """Verify a password against a hash.

        Args:
            password: Plain text password to verify
            password_hash: Hash to verify against

        Returns:
            True if password matches hash, False otherwise
        """
        return PasswordHasher.hash_password(password) == password_hash

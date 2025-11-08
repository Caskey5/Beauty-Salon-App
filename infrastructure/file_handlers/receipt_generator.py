"""Receipt generation service."""
from pathlib import Path
from datetime import datetime
from core.entities import Appointment


class ReceiptGenerator:
    """Generates receipt files for appointments."""

    def __init__(self, receipts_dir: Path):
        """Initialize receipt generator.

        Args:
            receipts_dir: Directory to save receipts
        """
        self.receipts_dir = receipts_dir
        self.receipts_dir.mkdir(parents=True, exist_ok=True)

    def generate(self, appointment: Appointment) -> Path:
        """Generate receipt file for appointment.

        Args:
            appointment: Appointment to generate receipt for

        Returns:
            Path to generated receipt file
        """
        # Format filename: receipt_FirstName_LastName_Date.txt
        filename = f"receipt_{appointment.first_name}_{appointment.last_name}_{appointment.date}.txt"
        file_path = self.receipts_dir / filename

        # Generate receipt content
        content = self._format_receipt(appointment)

        # Write to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return file_path

    def _format_receipt(self, appointment: Appointment) -> str:
        """Format receipt content.

        Args:
            appointment: Appointment details

        Returns:
            Formatted receipt text
        """
        return f"""
╔════════════════════════════════════════╗
║        BEAUTY SALON RECEIPT            ║
╚════════════════════════════════════════╝

Customer Information:
  Name: {appointment.full_name}
  Phone: {appointment.phone_number}

Appointment Details:
  Date: {appointment.date}
  Time: {appointment.time}
  Service: {appointment.service_name}

Payment Information:
  Service Price: {appointment.service_price}€

═══════════════════════════════════════════

Thank you for choosing our Beauty Salon!

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""

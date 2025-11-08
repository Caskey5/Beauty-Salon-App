"""Migration script to import CSV data into SQLite database."""
import csv
from pathlib import Path

from di_container import DIContainer


def migrate_users(container: DIContainer, csv_path: Path):
    """Migrate users from CSV to SQLite.

    Args:
        container: DI container
        csv_path: Path to users CSV file
    """
    if not csv_path.exists():
        print(f"[!] Users CSV not found: {csv_path}")
        return

    print(f"[*] Migrating users from {csv_path}...")

    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            # CSV format: Ime,Prezime,Broj,Nadimak,Lozinka
            reader = csv.DictReader(f)

            count = 0
            for row in reader:
                first_name = row.get('Ime', '').strip()
                last_name = row.get('Prezime', '').strip()
                phone = row.get('Broj', '').strip()
                username = row.get('Nadimak', '').strip()
                password_hash = row.get('Lozinka', '').strip()

                if not all([first_name, last_name, phone, username, password_hash]):
                    continue

                # Check if user already exists
                if container.user_repository.username_exists(username):
                    print(f"  [SKIP] User '{username}' already exists, skipping")
                    continue

                from core.entities import User
                user = User(
                    first_name=first_name,
                    last_name=last_name,
                    phone_number=phone,
                    username=username,
                    password_hash=password_hash,
                )

                container.user_repository.create(user)
                count += 1
                print(f"  [OK] Migrated user: {username}")

            print(f"[+] Successfully migrated {count} users\n")

    except Exception as e:
        print(f"[ERROR] Error migrating users: {e}\n")


def migrate_employees(container: DIContainer, csv_path: Path):
    """Migrate employees from CSV to SQLite.

    Args:
        container: DI container
        csv_path: Path to employees CSV file
    """
    if not csv_path.exists():
        print(f"[!] Employees CSV not found: {csv_path}")
        return

    print(f"[*] Migrating employees from {csv_path}...")

    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            # CSV format: Ime,Prezime,Pozicija,Broj,Nadimak,Lozinka
            reader = csv.DictReader(f)

            count = 0
            for row in reader:
                first_name = row.get('Ime', '').strip()
                last_name = row.get('Prezime', '').strip()
                position = row.get('Pozicija', '').strip()
                phone = row.get('Broj', '').strip()
                username = row.get('Nadimak', '').strip()
                password_hash = row.get('Lozinka', '').strip()

                if not all([first_name, last_name, position, phone, username, password_hash]):
                    continue

                # Check if employee already exists
                if container.employee_repository.username_exists(username):
                    print(f"  [SKIP] Employee '{username}' already exists, skipping")
                    continue

                from core.entities import Employee
                employee = Employee(
                    first_name=first_name,
                    last_name=last_name,
                    position=position,
                    phone_number=phone,
                    username=username,
                    password_hash=password_hash,
                )

                container.employee_repository.create(employee)
                count += 1
                print(f"  [OK] Migrated employee: {username}")

            print(f"[+] Successfully migrated {count} employees\n")

    except Exception as e:
        print(f"[ERROR] Error migrating employees: {e}\n")


def migrate_appointments(container: DIContainer, csv_path: Path):
    """Migrate appointments from CSV to SQLite.

    Args:
        container: DI container
        csv_path: Path to appointments CSV file
    """
    if not csv_path.exists():
        print(f"[!] Appointments CSV not found: {csv_path}")
        return

    print(f"[*] Migrating appointments from {csv_path}...")

    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            # CSV format: Ime,Prezime,Broj,Datum,Vrijeme,Zahvat
            reader = csv.DictReader(f)

            count = 0
            for row in reader:
                first_name = row.get('Ime', '').strip()
                last_name = row.get('Prezime', '').strip()
                phone = row.get('Broj', '').strip()
                date = row.get('Datum', '').strip()
                time = row.get('Vrijeme', '').strip()
                service_with_price = row.get('Zahvat', '').strip()

                if not all([first_name, last_name, phone, date, time, service_with_price]):
                    continue

                # Parse service and price
                # Format: "Service Name -> Price€" or "Service Name -> Price"
                if ' -> ' in service_with_price:
                    service_name, price_str = service_with_price.split(' -> ')
                    price_str = price_str.replace('€', '').strip()
                    try:
                        service_price = float(price_str)
                    except ValueError:
                        service_price = 0.0
                else:
                    service_name = service_with_price
                    service_price = 0.0

                # Normalize date format to YYYY-MM-DD
                if '-' in date:
                    parts = date.split('-')
                    if len(parts[0]) == 4:
                        # Already in YYYY-MM-DD format
                        normalized_date = date
                    else:
                        # DD-MM-YYYY format, convert to YYYY-MM-DD
                        normalized_date = f"{parts[2]}-{parts[1]}-{parts[0]}"
                else:
                    normalized_date = date

                # Skip if appointment already exists
                existing = container.appointment_repository.get_by_date_and_time(normalized_date, time)
                if existing:
                    print(f"  [SKIP] Appointment {normalized_date} {time} already exists, skipping")
                    continue

                from core.entities import Appointment
                appointment = Appointment(
                    first_name=first_name,
                    last_name=last_name,
                    phone_number=phone,
                    date=normalized_date,
                    time=time,
                    service_name=service_name,
                    service_price=service_price,
                )

                container.appointment_repository.create(appointment)
                count += 1
                print(f"  [OK] Migrated appointment: {first_name} {last_name} on {normalized_date} at {time}")

            print(f"[+] Successfully migrated {count} appointments\n")

    except Exception as e:
        print(f"[ERROR] Error migrating appointments: {e}\n")


def main():
    """Run data migration."""
    print("=" * 60)
    print(" " * 15 + "DATA MIGRATION TOOL")
    print(" " * 10 + "CSV -> SQLite Database")
    print("=" * 60)
    print()

    # Initialize container
    container = DIContainer()

    # CSV paths (old data directory)
    data_dir = Path("data")
    users_csv = data_dir / "korisnici.csv"
    employees_csv = data_dir / "zaposlenici.csv"
    appointments_csv = data_dir / "zakazani_termini.csv"

    # Run migrations
    migrate_users(container, users_csv)
    migrate_employees(container, employees_csv)
    migrate_appointments(container, appointments_csv)

    # Cleanup
    container.cleanup()

    print("=" * 60)
    print("[SUCCESS] Migration completed!")
    print(f"[INFO] Database location: {container.db_connection.database_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()

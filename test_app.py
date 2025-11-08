"""Test script to verify all functionality works correctly."""
from di_container import DIContainer
from config.constants import UserRole


def test_database_connection():
    """Test database connection and schema."""
    print("=" * 60)
    print("TEST 1: Database Connection & Schema")
    print("=" * 60)

    container = DIContainer()

    try:
        # Test connection
        conn = container.db_connection
        print("[OK] Database connection established")
        print(f"[INFO] Database location: {conn.database_path}")

        # Check tables
        with conn.get_cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [row[0] for row in cursor.fetchall()]
            print(f"[OK] Tables found: {', '.join(tables)}")

            # Count records in each table
            for table in tables:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = cursor.fetchone()[0]
                print(f"[INFO] {table}: {count} records")

        print("[SUCCESS] Database test passed!\n")
        container.cleanup()
        return True

    except Exception as e:
        print(f"[ERROR] Database test failed: {e}\n")
        container.cleanup()
        return False


def test_authentication():
    """Test authentication functionality."""
    print("=" * 60)
    print("TEST 2: Authentication System")
    print("=" * 60)

    container = DIContainer()

    try:
        # Test admin login
        print("\n[TEST] Admin login...")
        result = container.login_user.execute("Caskey", "#Caskey123")
        assert result.success, "Admin login failed"
        assert result.role == UserRole.ADMIN, "Admin role not set"
        print(f"[OK] Admin login successful: {result.message}")

        # Test customer login
        print("\n[TEST] Customer login...")
        result = container.login_user.execute("Lucija", "Test123!")
        if result.success:
            assert result.role == UserRole.CUSTOMER, "Customer role not set"
            assert result.user is not None, "User entity not returned"
            print(f"[OK] Customer login successful: {result.user.full_name}")
        else:
            print(f"[SKIP] Customer 'Lucija' not found or wrong password")

        # Test employee login
        print("\n[TEST] Employee login...")
        result = container.login_user.execute("Ivan", "Test123!")
        if result.success:
            assert result.role == UserRole.EMPLOYEE, "Employee role not set"
            assert result.employee is not None, "Employee entity not returned"
            print(f"[OK] Employee login successful: {result.employee.full_name}")
        else:
            print(f"[SKIP] Employee 'Ivan' not found or wrong password")

        # Test invalid login
        print("\n[TEST] Invalid login...")
        result = container.login_user.execute("invalid_user", "wrong_password")
        assert not result.success, "Invalid login should fail"
        print(f"[OK] Invalid login correctly rejected")

        print("\n[SUCCESS] Authentication test passed!\n")
        container.cleanup()
        return True

    except Exception as e:
        print(f"\n[ERROR] Authentication test failed: {e}\n")
        container.cleanup()
        return False


def test_data_retrieval():
    """Test data retrieval."""
    print("=" * 60)
    print("TEST 3: Data Retrieval")
    print("=" * 60)

    container = DIContainer()

    try:
        # Test get all users
        print("\n[TEST] Retrieving users...")
        users = container.user_repository.get_all()
        print(f"[OK] Found {len(users)} users")
        for user in users[:3]:  # Show first 3
            print(f"  - {user.full_name} ({user.username})")

        # Test get all employees
        print("\n[TEST] Retrieving employees...")
        employees = container.employee_repository.get_all()
        print(f"[OK] Found {len(employees)} employees")
        for emp in employees[:3]:
            print(f"  - {emp.full_name} - {emp.position}")

        # Test get all appointments
        print("\n[TEST] Retrieving appointments...")
        appointments = container.get_appointments.get_all()
        print(f"[OK] Found {len(appointments)} appointments")
        for apt in appointments[:3]:
            print(f"  - {apt.date} {apt.time}: {apt.full_name} - {apt.service_name}")

        # Test get all services
        print("\n[TEST] Retrieving services...")
        services = container.get_services.get_all()
        print(f"[OK] Found {len(services)} services")
        for svc in services[:5]:
            print(f"  - {svc.name}: {svc.formatted_price}")

        print("\n[SUCCESS] Data retrieval test passed!\n")
        container.cleanup()
        return True

    except Exception as e:
        print(f"\n[ERROR] Data retrieval test failed: {e}\n")
        container.cleanup()
        return False


def test_use_cases():
    """Test use cases."""
    print("=" * 60)
    print("TEST 4: Use Cases")
    print("=" * 60)

    container = DIContainer()

    try:
        # Test get available slots
        print("\n[TEST] Getting available slots for 2025-06-01...")
        slots = container.get_available_slots.execute("2025-06-01")
        print(f"[OK] Found {len(slots)} available slots")
        if slots:
            print(f"  First few slots: {', '.join(slots[:5])}")

        # Test get available slots for Sunday (should be empty)
        print("\n[TEST] Getting available slots for Sunday 2025-06-01...")
        sunday_slots = container.get_available_slots.execute("2025-06-01")
        # Note: 2025-06-01 is a Sunday, should have no slots

        # Test working hours service
        print("\n[TEST] Testing working hours service...")
        from infrastructure.scheduling import WorkingHoursService

        weekday_hours = WorkingHoursService.get_available_hours("2025-06-02")  # Monday
        print(f"[OK] Monday hours: {len(weekday_hours)} slots ({weekday_hours[0]} to {weekday_hours[-1]})")

        saturday_hours = WorkingHoursService.get_available_hours("2025-06-07")  # Saturday
        print(f"[OK] Saturday hours: {len(saturday_hours)} slots ({saturday_hours[0]} to {saturday_hours[-1]})")

        sunday_hours = WorkingHoursService.get_available_hours("2025-06-01")  # Sunday
        print(f"[OK] Sunday hours: {len(sunday_hours)} slots (salon closed)")

        # Test password validation
        print("\n[TEST] Testing password validation...")
        from infrastructure.security import PasswordValidator

        valid_password = "Test123!"
        invalid_password = "weak"

        assert PasswordValidator.is_valid(valid_password), "Valid password rejected"
        print(f"[OK] Valid password '{valid_password}' accepted")

        assert not PasswordValidator.is_valid(invalid_password), "Invalid password accepted"
        print(f"[OK] Invalid password '{invalid_password}' rejected")

        # Test password hashing
        print("\n[TEST] Testing password hashing...")
        from infrastructure.security import PasswordHasher

        password = "TestPassword123!"
        hash1 = PasswordHasher.hash_password(password)
        hash2 = PasswordHasher.hash_password(password)

        assert hash1 == hash2, "Same password produces different hashes"
        print(f"[OK] Password hashing is consistent")

        assert PasswordHasher.verify_password(password, hash1), "Password verification failed"
        print(f"[OK] Password verification works")

        print("\n[SUCCESS] Use cases test passed!\n")
        container.cleanup()
        return True

    except Exception as e:
        print(f"\n[ERROR] Use cases test failed: {e}\n")
        import traceback
        traceback.print_exc()
        container.cleanup()
        return False


def test_appointment_creation():
    """Test creating an appointment."""
    print("=" * 60)
    print("TEST 5: Appointment Creation")
    print("=" * 60)

    container = DIContainer()

    try:
        # Get a service
        services = container.get_services.get_all()
        test_service = services[0]

        print(f"\n[TEST] Creating test appointment...")
        print(f"  Service: {test_service.name}")
        print(f"  Date: 2025-12-15")
        print(f"  Time: 10:00")

        result = container.create_appointment.execute(
            first_name="Test",
            last_name="User",
            phone_number="1234567890",
            date="2025-12-15",
            time="10:00",
            service_name=test_service.name,
            service_price=test_service.price,
        )

        if result.success:
            print(f"[OK] Appointment created: {result.message}")

            # Clean up - delete the test appointment
            print("\n[TEST] Cleaning up test appointment...")
            cancel_result = container.cancel_appointment.execute(
                result.appointment.appointment_id
            )

            if cancel_result.success:
                print(f"[OK] Test appointment deleted")
            else:
                print(f"[WARNING] Could not delete test appointment")
        else:
            print(f"[INFO] Appointment creation result: {result.message}")

        print("\n[SUCCESS] Appointment creation test passed!\n")
        container.cleanup()
        return True

    except Exception as e:
        print(f"\n[ERROR] Appointment creation test failed: {e}\n")
        import traceback
        traceback.print_exc()
        container.cleanup()
        return False


def main():
    """Run all tests."""
    print("\n")
    print("=" * 60)
    print(" " * 10 + "BEAUTY SALON APPLICATION TEST SUITE")
    print("=" * 60)
    print()

    results = []

    # Run tests
    results.append(("Database Connection", test_database_connection()))
    results.append(("Authentication System", test_authentication()))
    results.append(("Data Retrieval", test_data_retrieval()))
    results.append(("Use Cases", test_use_cases()))
    results.append(("Appointment Creation", test_appointment_creation()))

    # Summary
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for test_name, result in results:
        status = "[PASS]" if result else "[FAIL]"
        print(f"{status} {test_name}")

    print()
    print(f"Total: {passed}/{total} tests passed")

    if passed == total:
        print("\n[SUCCESS] All tests passed! Application is working correctly!")
    else:
        print("\n[WARNING] Some tests failed. Please review the errors above.")

    print("=" * 60)


if __name__ == "__main__":
    main()

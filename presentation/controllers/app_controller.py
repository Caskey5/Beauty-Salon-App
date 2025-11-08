"""Application controller - manages navigation and screen transitions."""
import tkinter as tk
from typing import Optional

from di_container import DIContainer
from core.entities import User, Employee
from config.constants import UserRole


class AppController:
    """Main application controller.

    Manages screen navigation and state transitions.
    """

    def __init__(self, root: tk.Tk, container: DIContainer):
        """Initialize controller.

        Args:
            root: Root Tkinter window
            container: Dependency injection container
        """
        self.root = root
        self.container = container

        # Current state
        self.current_frame: Optional[tk.Frame] = None
        self.current_user: Optional[User] = None
        self.current_employee: Optional[Employee] = None
        self.current_role: Optional[UserRole] = None

    def clear_frame(self) -> None:
        """Clear the current frame."""
        if self.current_frame:
            self.current_frame.destroy()
            self.current_frame = None

    def show_main_screen(self) -> None:
        """Show main screen with login/signup buttons."""
        from presentation.components.main_screen import MainScreen

        self.clear_frame()
        self.current_frame = MainScreen(self.root, self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_login(self) -> None:
        """Show login screen."""
        from presentation.components.login_view import LoginView

        self.clear_frame()
        self.current_frame = LoginView(self.root, self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_signup(self) -> None:
        """Show signup screen."""
        from presentation.components.signup_view import SignupView

        self.clear_frame()
        self.current_frame = SignupView(self.root, self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def on_login_success(
        self, role: UserRole, user: Optional[User] = None, employee: Optional[Employee] = None
    ) -> None:
        """Handle successful login.

        Args:
            role: User role
            user: User entity (for customers)
            employee: Employee entity (for employees)
        """
        self.current_role = role
        self.current_user = user
        self.current_employee = employee

        # Navigate to appropriate dashboard
        if role == UserRole.ADMIN:
            self.show_admin_dashboard()
        elif role == UserRole.CUSTOMER:
            self.show_customer_dashboard()
        elif role == UserRole.EMPLOYEE:
            self.show_employee_dashboard()

    def show_admin_dashboard(self) -> None:
        """Show admin dashboard."""
        from presentation.dashboards.admin_dashboard import AdminDashboard

        self.clear_frame()
        self.current_frame = AdminDashboard(self.root, self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_customer_dashboard(self) -> None:
        """Show customer dashboard."""
        from presentation.dashboards.customer_dashboard import CustomerDashboard

        if not self.current_user:
            self.show_main_screen()
            return

        self.clear_frame()
        self.current_frame = CustomerDashboard(self.root, self, self.current_user)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_employee_dashboard(self) -> None:
        """Show employee dashboard."""
        from presentation.dashboards.employee_dashboard import EmployeeDashboard

        if not self.current_employee:
            self.show_main_screen()
            return

        self.clear_frame()
        self.current_frame = EmployeeDashboard(self.root, self, self.current_employee)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def logout(self) -> None:
        """Logout and return to main screen."""
        self.current_user = None
        self.current_employee = None
        self.current_role = None
        self.show_main_screen()

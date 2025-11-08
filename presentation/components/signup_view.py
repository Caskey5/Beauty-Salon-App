"""Signup view component."""
import tkinter as tk
from tkinter import messagebox
from config.settings import settings
from config.constants import Messages


class SignupView(tk.Frame):
    """Signup view for new user registration."""

    def __init__(self, parent: tk.Tk, controller):
        """Initialize signup view.

        Args:
            parent: Parent window
            controller: Application controller
        """
        super().__init__(parent, bg=settings.BACKGROUND_COLOR)
        self.controller = controller
        self.container = controller.container

        self._create_widgets()

    def _create_widgets(self) -> None:
        """Create and layout widgets."""
        # Main frame
        frame = tk.Frame(self, bg="light salmon", width=450, height=500)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        title_label = tk.Label(
            frame,
            text="Sign Up",
            font=("Helvetica", 18, "bold"),
            bg="light salmon"
        )
        title_label.pack(pady=15)

        # First name
        first_name_label = tk.Label(
            frame, text="First Name:", font=("Helvetica", 11), bg="light salmon"
        )
        first_name_label.pack(pady=3)
        self.first_name_entry = tk.Entry(frame, font=("Helvetica", 11), width=30)
        self.first_name_entry.pack(pady=3)

        # Last name
        last_name_label = tk.Label(
            frame, text="Last Name:", font=("Helvetica", 11), bg="light salmon"
        )
        last_name_label.pack(pady=3)
        self.last_name_entry = tk.Entry(frame, font=("Helvetica", 11), width=30)
        self.last_name_entry.pack(pady=3)

        # Phone number
        phone_label = tk.Label(
            frame, text="Phone Number:", font=("Helvetica", 11), bg="light salmon"
        )
        phone_label.pack(pady=3)
        self.phone_entry = tk.Entry(frame, font=("Helvetica", 11), width=30)
        self.phone_entry.pack(pady=3)

        # Username
        username_label = tk.Label(
            frame, text="Username:", font=("Helvetica", 11), bg="light salmon"
        )
        username_label.pack(pady=3)
        self.username_entry = tk.Entry(frame, font=("Helvetica", 11), width=30)
        self.username_entry.pack(pady=3)

        # Password
        password_label = tk.Label(
            frame, text="Password:", font=("Helvetica", 11), bg="light salmon"
        )
        password_label.pack(pady=3)
        self.password_entry = tk.Entry(
            frame, font=("Helvetica", 11), width=30, show="*"
        )
        self.password_entry.pack(pady=3)

        # Confirm password
        confirm_password_label = tk.Label(
            frame, text="Confirm Password:", font=("Helvetica", 11), bg="light salmon"
        )
        confirm_password_label.pack(pady=3)
        self.confirm_password_entry = tk.Entry(
            frame, font=("Helvetica", 11), width=30, show="*"
        )
        self.confirm_password_entry.pack(pady=3)

        # Buttons frame
        buttons_frame = tk.Frame(frame, bg="light salmon")
        buttons_frame.pack(pady=15)

        # Register button
        register_btn = tk.Button(
            buttons_frame,
            text="Register",
            font=("Helvetica", 12),
            width=10,
            command=self._handle_signup,
            cursor="hand2"
        )
        register_btn.pack(side=tk.LEFT, padx=5)

        # Back button
        back_btn = tk.Button(
            buttons_frame,
            text="Back",
            font=("Helvetica", 12),
            width=10,
            command=self.controller.show_main_screen,
            cursor="hand2"
        )
        back_btn.pack(side=tk.LEFT, padx=5)

        # Bind Enter key to register
        self.confirm_password_entry.bind("<Return>", lambda e: self._handle_signup())

    def _handle_signup(self) -> None:
        """Handle signup button click."""
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        confirm_password = self.confirm_password_entry.get().strip()

        # Execute register use case
        register_use_case = self.container.register_user
        result = register_use_case.execute(
            first_name, last_name, phone, username, password, confirm_password
        )

        if result.success:
            messagebox.showinfo("Success", result.message)
            self.controller.show_login()
        else:
            messagebox.showerror("Registration Failed", result.message)

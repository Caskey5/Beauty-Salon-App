"""Login view component."""
import tkinter as tk
from tkinter import messagebox
from config.settings import settings
from config.constants import Messages


class LoginView(tk.Frame):
    """Login view for user authentication."""

    def __init__(self, parent: tk.Tk, controller):
        """Initialize login view.

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
        frame = tk.Frame(self, bg="light salmon", width=400, height=300)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        title_label = tk.Label(
            frame,
            text="Login",
            font=("Helvetica", 18, "bold"),
            bg="light salmon"
        )
        title_label.pack(pady=20)

        # Username field
        username_label = tk.Label(
            frame, text="Username:", font=("Helvetica", 12), bg="light salmon"
        )
        username_label.pack(pady=5)

        self.username_entry = tk.Entry(frame, font=("Helvetica", 12), width=25)
        self.username_entry.pack(pady=5)

        # Password field
        password_label = tk.Label(
            frame, text="Password:", font=("Helvetica", 12), bg="light salmon"
        )
        password_label.pack(pady=5)

        self.password_entry = tk.Entry(
            frame, font=("Helvetica", 12), width=25, show="*"
        )
        self.password_entry.pack(pady=5)

        # Buttons frame
        buttons_frame = tk.Frame(frame, bg="light salmon")
        buttons_frame.pack(pady=20)

        # Login button
        login_btn = tk.Button(
            buttons_frame,
            text="Login",
            font=("Helvetica", 12),
            width=10,
            command=self._handle_login,
            cursor="hand2"
        )
        login_btn.pack(side=tk.LEFT, padx=5)

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

        # Bind Enter key to login
        self.password_entry.bind("<Return>", lambda e: self._handle_login())

    def _handle_login(self) -> None:
        """Handle login button click."""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", Messages.MISSING_FIELDS)
            return

        # Execute login use case
        login_use_case = self.container.login_user
        result = login_use_case.execute(username, password)

        if result.success:
            messagebox.showinfo("Success", result.message)
            self.controller.on_login_success(
                result.role, result.user, result.employee
            )
        else:
            messagebox.showerror("Login Failed", result.message)
            self.password_entry.delete(0, tk.END)

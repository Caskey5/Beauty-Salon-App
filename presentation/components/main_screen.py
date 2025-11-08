"""Main screen with login/signup buttons."""
import tkinter as tk
from config.settings import settings


class MainScreen(tk.Frame):
    """Main screen with login and signup options."""

    def __init__(self, parent: tk.Tk, controller):
        """Initialize main screen.

        Args:
            parent: Parent window
            controller: Application controller
        """
        super().__init__(parent, bg=settings.BACKGROUND_COLOR)
        self.controller = controller

        self._create_widgets()

    def _create_widgets(self) -> None:
        """Create and layout widgets."""
        # Signup button
        signup_btn = tk.Button(
            self,
            text="Sign Up",
            font=("Helvetica", 14),
            width=12,
            command=self.controller.show_signup,
            cursor="hand2"
        )
        signup_btn.place(relx=0.5, rely=0.4, anchor="center")

        # Login button
        login_btn = tk.Button(
            self,
            text="Login",
            font=("Helvetica", 14),
            width=12,
            command=self.controller.show_login,
            cursor="hand2"
        )
        login_btn.place(relx=0.5, rely=0.5, anchor="center")

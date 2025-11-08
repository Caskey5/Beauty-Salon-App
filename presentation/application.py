"""Main application class - orchestrates the entire UI."""
import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk
from typing import Optional

from di_container import DIContainer
from config.settings import settings
from config.constants import Messages
from presentation.controllers.app_controller import AppController


class BeautySalonApplication:
    """Main application class.

    Manages the main window, navigation, and application lifecycle.
    """

    def __init__(self, container: DIContainer):
        """Initialize the application.

        Args:
            container: Dependency injection container
        """
        self.container = container
        self.root = tk.Tk()
        self.controller: Optional[AppController] = None

        self._setup_window()
        self._setup_background()
        self._initialize_controller()
        self._show_welcome_screen()

    def _setup_window(self) -> None:
        """Configure main window properties."""
        self.root.title(settings.WINDOW_TITLE)
        self.root.geometry(f"{settings.WINDOW_WIDTH}x{settings.WINDOW_HEIGHT}")
        self.root.resizable(True, True)

    def _setup_background(self) -> None:
        """Setup background image or fallback color."""
        try:
            if settings.BACKGROUND_IMAGE.exists():
                bg_image = Image.open(settings.BACKGROUND_IMAGE)
                bg_image = bg_image.resize(
                    (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
                )
                self.bg_photo = ImageTk.PhotoImage(bg_image)

                self.bg_label = tk.Label(self.root, image=self.bg_photo)
                self.bg_label.image = self.bg_photo
                self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            else:
                self.root.configure(bg=settings.BACKGROUND_COLOR)
        except Exception:
            # Fallback to solid color if image fails to load
            self.root.configure(bg=settings.BACKGROUND_COLOR)

    def _initialize_controller(self) -> None:
        """Initialize the application controller."""
        self.controller = AppController(self.root, self.container)

    def _show_welcome_screen(self) -> None:
        """Display welcome message and transition to main screen."""
        welcome_label = tk.Label(
            self.root,
            text=Messages.WELCOME_MESSAGE,
            font=("Helvetica", 20, "bold"),
            fg="black",
            bg=settings.BACKGROUND_COLOR
        )
        welcome_label.place(relx=0.5, rely=0.4, anchor="center")

        # Show login/signup buttons after 2 seconds
        self.root.after(2000, lambda: self._transition_to_main(welcome_label))

    def _transition_to_main(self, welcome_label: tk.Label) -> None:
        """Transition from welcome screen to main screen.

        Args:
            welcome_label: Welcome label to remove
        """
        welcome_label.destroy()
        if self.controller:
            self.controller.show_main_screen()

    def run(self) -> None:
        """Start the application main loop."""
        self.root.mainloop()

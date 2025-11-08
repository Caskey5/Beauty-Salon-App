"""Customer dashboard - self-service appointment management."""
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import Calendar

from config.settings import settings
from core.entities import User


class CustomerDashboard(tk.Frame):
    """Customer dashboard for booking and managing appointments."""

    def __init__(self, parent: tk.Tk, controller, user: User):
        """Initialize customer dashboard.

        Args:
            parent: Parent window
            controller: Application controller
            user: Logged in user
        """
        super().__init__(parent, bg=settings.BACKGROUND_COLOR)
        self.controller = controller
        self.container = controller.container
        self.user = user
        self.last_booked_appointment = None

        self._create_main_menu()

    def _create_main_menu(self) -> None:
        """Create main menu with action buttons."""
        for widget in self.winfo_children():
            widget.destroy()

        frame = tk.Frame(self, bg="light salmon", width=450, height=400)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Welcome message
        tk.Label(
            frame,
            text=f"Welcome, {self.user.first_name}!",
            font=("Helvetica", 20, "bold"),
            bg="light salmon"
        ).pack(pady=20)

        # Menu buttons
        buttons = [
            ("Book Appointment", self._show_book_appointment),
            ("My Appointments", self._show_my_appointments),
            ("Cancel Appointment", self._show_cancel_appointment),
            ("Logout", self.controller.logout),
        ]

        for text, command in buttons:
            tk.Button(
                frame, text=text, font=("Helvetica", 13), width=20,
                command=command, cursor="hand2"
            ).pack(pady=10)

    def _show_book_appointment(self) -> None:
        """Show book appointment screen."""
        for widget in self.winfo_children():
            widget.destroy()

        main_frame = tk.Frame(self, bg="light salmon")
        main_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            main_frame, text="Book Appointment", font=("Helvetica", 18, "bold"), bg="light salmon"
        ).pack(pady=15)

        # Calendar
        tk.Label(main_frame, text="Select Date:", font=("Helvetica", 12), bg="light salmon").pack(pady=5)

        cal = Calendar(
            main_frame,
            selectmode='day',
            date_pattern='yyyy-mm-dd',
            mindate=datetime.now().date()
        )
        cal.pack(pady=10)

        # Time selection
        tk.Label(main_frame, text="Select Time:", font=("Helvetica", 12), bg="light salmon").pack(pady=5)

        time_var = tk.StringVar()
        time_combo = ttk.Combobox(
            main_frame, textvariable=time_var, font=("Helvetica", 11),
            width=15, state="readonly"
        )
        time_combo.pack(pady=5)

        # Update available times when date changes
        def update_times(event=None):
            selected_date = cal.get_date()
            available = self.container.get_available_slots.execute(selected_date)
            time_combo['values'] = available
            if available:
                time_combo.current(0)
            else:
                messagebox.showinfo("Info", "No available slots for this date")

        cal.bind("<<CalendarSelected>>", update_times)
        update_times()

        # Service selection
        tk.Label(main_frame, text="Select Service:", font=("Helvetica", 12), bg="light salmon").pack(pady=5)

        service_var = tk.StringVar()
        service_combo = ttk.Combobox(
            main_frame, textvariable=service_var, font=("Helvetica", 11),
            width=30, state="readonly",
            values=self.container.get_services.get_display_names()
        )
        service_combo.pack(pady=5)

        # Buttons
        btn_frame = tk.Frame(main_frame, bg="light salmon")
        btn_frame.pack(pady=15)

        tk.Button(
            btn_frame, text="Book", font=("Helvetica", 12), width=10,
            command=lambda: self._handle_book_appointment(cal, time_var, service_var),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            btn_frame, text="Back", font=("Helvetica", 12), width=10,
            command=self._create_main_menu, cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)

    def _handle_book_appointment(
        self, cal: Calendar, time_var: tk.StringVar, service_var: tk.StringVar
    ) -> None:
        """Handle book appointment action."""
        service_display = service_var.get()
        if not service_display:
            messagebox.showerror("Error", "Please select a service")
            return

        time_slot = time_var.get()
        if not time_slot:
            messagebox.showerror("Error", "Please select a time slot")
            return

        # Parse service name and price
        service_name, price_str = service_display.split(" -> ")
        price = float(price_str.replace("€", ""))

        result = self.container.create_appointment.execute(
            first_name=self.user.first_name,
            last_name=self.user.last_name,
            phone_number=self.user.phone_number,
            date=cal.get_date(),
            time=time_slot,
            service_name=service_name,
            service_price=price,
        )

        if result.success:
            self.last_booked_appointment = result.appointment
            self._show_confirmation()
        else:
            messagebox.showerror("Error", result.message)

    def _show_confirmation(self) -> None:
        """Show booking confirmation with receipt option."""
        if not self.last_booked_appointment:
            self._create_main_menu()
            return

        for widget in self.winfo_children():
            widget.destroy()

        frame = tk.Frame(self, bg="light salmon", width=450, height=400)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            frame, text="Booking Confirmed!",
            font=("Helvetica", 20, "bold"), bg="light salmon", fg="green"
        ).pack(pady=20)

        apt = self.last_booked_appointment

        # Appointment details
        details_text = f"""
Date: {apt.date}
Time: {apt.time}
Service: {apt.service_name}
Price: {apt.service_price}€
        """

        tk.Label(
            frame, text=details_text, font=("Helvetica", 12),
            bg="light salmon", justify=tk.LEFT
        ).pack(pady=10)

        # Buttons
        tk.Button(
            frame, text="Generate Receipt", font=("Helvetica", 12), width=15,
            command=self._generate_receipt, cursor="hand2"
        ).pack(pady=10)

        tk.Button(
            frame, text="Back to Menu", font=("Helvetica", 12), width=15,
            command=self._create_main_menu, cursor="hand2"
        ).pack(pady=5)

    def _generate_receipt(self) -> None:
        """Generate receipt for last booked appointment."""
        if not self.last_booked_appointment:
            return

        try:
            receipt_path = self.container.receipt_generator.generate(
                self.last_booked_appointment
            )
            messagebox.showinfo(
                "Receipt Generated",
                f"Receipt saved to:\n{receipt_path}"
            )
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate receipt: {str(e)}")

    def _show_my_appointments(self) -> None:
        """Show user's appointments."""
        for widget in self.winfo_children():
            widget.destroy()

        frame = tk.Frame(self, bg="light salmon")
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(
            frame, text="My Appointments", font=("Helvetica", 18, "bold"), bg="light salmon"
        ).pack(pady=15)

        # Text widget with scrollbar
        text_frame = tk.Frame(frame)
        text_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_widget = tk.Text(
            text_frame, font=("Courier", 11), height=15, width=60,
            yscrollcommand=scrollbar.set
        )
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=text_widget.yview)

        # Load user's appointments
        appointments = self.container.get_appointments.get_by_customer(
            self.user.first_name, self.user.last_name, self.user.phone_number
        )

        if appointments:
            for apt in appointments:
                text_widget.insert(
                    tk.END,
                    f"{apt.date} at {apt.time}\n"
                    f"Service: {apt.service_name}\n"
                    f"Price: {apt.service_price}€\n"
                    f"{'-' * 40}\n"
                )
        else:
            text_widget.insert(tk.END, "No appointments found.")

        text_widget.config(state=tk.DISABLED)

        # Back button
        tk.Button(
            frame, text="Back", font=("Helvetica", 12), width=10,
            command=self._create_main_menu, cursor="hand2"
        ).pack(pady=10)

    def _show_cancel_appointment(self) -> None:
        """Show cancel appointment screen."""
        for widget in self.winfo_children():
            widget.destroy()

        frame = tk.Frame(self, bg="light salmon")
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(
            frame, text="Cancel Appointment", font=("Helvetica", 18, "bold"), bg="light salmon"
        ).pack(pady=15)

        # Appointments list
        listbox = tk.Listbox(frame, font=("Helvetica", 11), height=12, width=60)
        listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        appointments = self.container.get_appointments.get_by_customer(
            self.user.first_name, self.user.last_name, self.user.phone_number
        )
        appointment_map = {}

        if appointments:
            for apt in appointments:
                display = f"{apt.date} {apt.time} - {apt.service_name}"
                listbox.insert(tk.END, display)
                appointment_map[display] = apt
        else:
            listbox.insert(tk.END, "No appointments to cancel")

        # Buttons
        btn_frame = tk.Frame(frame, bg="light salmon")
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame, text="Cancel Selected", font=("Helvetica", 12), width=15,
            command=lambda: self._handle_cancel_appointment(listbox, appointment_map),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            btn_frame, text="Back", font=("Helvetica", 12), width=10,
            command=self._create_main_menu, cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)

    def _handle_cancel_appointment(self, listbox: tk.Listbox, appointment_map: dict) -> None:
        """Handle cancel appointment action."""
        selection = listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an appointment to cancel")
            return

        display = listbox.get(selection[0])
        if display == "No appointments to cancel":
            return

        appointment = appointment_map[display]

        confirm = messagebox.askyesno(
            "Confirm", f"Cancel appointment on {appointment.date} at {appointment.time}?"
        )
        if not confirm:
            return

        result = self.container.cancel_appointment.execute(appointment.appointment_id)

        if result.success:
            messagebox.showinfo("Success", result.message)
            self._show_cancel_appointment()
        else:
            messagebox.showerror("Error", result.message)

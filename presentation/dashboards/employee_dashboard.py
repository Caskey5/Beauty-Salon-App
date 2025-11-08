"""Employee dashboard - appointment management for staff."""
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import Calendar

from config.settings import settings
from core.entities import Employee


class EmployeeDashboard(tk.Frame):
    """Employee dashboard for managing salon appointments."""

    def __init__(self, parent: tk.Tk, controller, employee: Employee):
        """Initialize employee dashboard.

        Args:
            parent: Parent window
            controller: Application controller
            employee: Logged in employee
        """
        super().__init__(parent, bg=settings.BACKGROUND_COLOR)
        self.controller = controller
        self.container = controller.container
        self.employee = employee

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
            text=f"Employee: {self.employee.full_name}",
            font=("Helvetica", 18, "bold"),
            bg="light salmon"
        ).pack(pady=15)

        tk.Label(
            frame,
            text=f"Position: {self.employee.position}",
            font=("Helvetica", 12),
            bg="light salmon"
        ).pack(pady=5)

        # Menu buttons
        buttons = [
            ("Schedule Appointment", self._show_schedule_appointment),
            ("Cancel Appointment", self._show_cancel_appointment),
            ("View All Appointments", self._show_all_appointments),
            ("Logout", self.controller.logout),
        ]

        for text, command in buttons:
            tk.Button(
                frame, text=text, font=("Helvetica", 13), width=22,
                command=command, cursor="hand2"
            ).pack(pady=10)

    def _show_schedule_appointment(self) -> None:
        """Show schedule appointment screen."""
        for widget in self.winfo_children():
            widget.destroy()

        main_frame = tk.Frame(self, bg="light salmon")
        main_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            main_frame, text="Schedule Appointment", font=("Helvetica", 18, "bold"), bg="light salmon"
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

        # Customer info button
        customer_data = {}

        def get_customer_info():
            """Get customer information via popup."""
            popup = tk.Toplevel(self)
            popup.title("Customer Information")
            popup.geometry("300x250")
            popup.resizable(False, False)

            tk.Label(popup, text="First Name:", font=("Helvetica", 10)).pack(pady=3)
            first_name_entry = tk.Entry(popup, font=("Helvetica", 10), width=25)
            first_name_entry.pack(pady=3)

            tk.Label(popup, text="Last Name:", font=("Helvetica", 10)).pack(pady=3)
            last_name_entry = tk.Entry(popup, font=("Helvetica", 10), width=25)
            last_name_entry.pack(pady=3)

            tk.Label(popup, text="Phone:", font=("Helvetica", 10)).pack(pady=3)
            phone_entry = tk.Entry(popup, font=("Helvetica", 10), width=25)
            phone_entry.pack(pady=3)

            def save_info():
                customer_data['first_name'] = first_name_entry.get().strip()
                customer_data['last_name'] = last_name_entry.get().strip()
                customer_data['phone'] = phone_entry.get().strip()
                popup.destroy()

            tk.Button(popup, text="Save", font=("Helvetica", 10), command=save_info).pack(pady=10)

        tk.Button(
            main_frame, text="Enter Customer Info", font=("Helvetica", 11),
            command=get_customer_info, cursor="hand2"
        ).pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(main_frame, bg="light salmon")
        btn_frame.pack(pady=15)

        tk.Button(
            btn_frame, text="Book", font=("Helvetica", 12), width=10,
            command=lambda: self._handle_schedule_appointment(
                cal, time_var, service_var, customer_data
            ), cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            btn_frame, text="Back", font=("Helvetica", 12), width=10,
            command=self._create_main_menu, cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)

    def _handle_schedule_appointment(
        self, cal: Calendar, time_var: tk.StringVar, service_var: tk.StringVar, customer_data: dict
    ) -> None:
        """Handle schedule appointment action."""
        if not customer_data:
            messagebox.showerror("Error", "Please enter customer information")
            return

        service_display = service_var.get()
        if not service_display:
            messagebox.showerror("Error", "Please select a service")
            return

        # Parse service name and price
        service_name, price_str = service_display.split(" -> ")
        price = float(price_str.replace("€", ""))

        result = self.container.create_appointment.execute(
            first_name=customer_data.get('first_name', ''),
            last_name=customer_data.get('last_name', ''),
            phone_number=customer_data.get('phone', ''),
            date=cal.get_date(),
            time=time_var.get(),
            service_name=service_name,
            service_price=price,
        )

        if result.success:
            messagebox.showinfo("Success", result.message)
            self._create_main_menu()
        else:
            messagebox.showerror("Error", result.message)

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
        listbox = tk.Listbox(frame, font=("Helvetica", 10), height=15, width=70)
        listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        appointments = self.container.get_appointments.get_all()
        appointment_map = {}

        for apt in appointments:
            display = f"{apt.date} {apt.time} - {apt.full_name} - {apt.service_name}"
            listbox.insert(tk.END, display)
            appointment_map[display] = apt

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
        appointment = appointment_map[display]

        confirm = messagebox.askyesno(
            "Confirm", f"Cancel appointment for {appointment.full_name}?"
        )
        if not confirm:
            return

        result = self.container.cancel_appointment.execute(appointment.appointment_id)

        if result.success:
            messagebox.showinfo("Success", result.message)
            self._show_cancel_appointment()
        else:
            messagebox.showerror("Error", result.message)

    def _show_all_appointments(self) -> None:
        """Show all appointments."""
        for widget in self.winfo_children():
            widget.destroy()

        frame = tk.Frame(self, bg="light salmon")
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(
            frame, text="All Appointments", font=("Helvetica", 18, "bold"), bg="light salmon"
        ).pack(pady=15)

        # Text widget with scrollbar
        text_frame = tk.Frame(frame)
        text_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_widget = tk.Text(
            text_frame, font=("Courier", 10), height=20, width=80,
            yscrollcommand=scrollbar.set
        )
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=text_widget.yview)

        # Load appointments
        appointments = self.container.get_appointments.get_all()

        for apt in appointments:
            text_widget.insert(
                tk.END,
                f"{apt.date} {apt.time} | {apt.full_name} | {apt.phone_number} | "
                f"{apt.service_name} ({apt.service_price}€)\n"
            )

        text_widget.config(state=tk.DISABLED)

        # Back button
        tk.Button(
            frame, text="Back", font=("Helvetica", 12), width=10,
            command=self._create_main_menu, cursor="hand2"
        ).pack(pady=10)

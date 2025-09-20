import csv
import os
import hashlib
from tkinter import messagebox

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def load_services_from_csv():
    """Load services from CSV file with error handling"""
    services = []
    try:
        with open("data/usluge.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                services.append(f"{row['Usluga']} -> {row['Cijena']}")
    except FileNotFoundError:
        messagebox.showerror("Greška", "Nije moguće učitati usluge.")
    except (UnicodeDecodeError, KeyError):
        messagebox.showerror("Greška", "Podaci o uslugama su oštećeni.")
    return services

def get_working_hours(selected_date):
    """Get working hours based on selected date"""
    import datetime
    try:
        day, month, year = map(int, selected_date.split("-"))
        dt = datetime.date(year, month, day)
    except (ValueError, AttributeError):
        return []
    
    if dt.weekday() == 6:  # Sunday
        return []  # Closed on Sunday
    elif dt.weekday() == 5:  # Saturday
        return [f"{i:02d}:00" for i in range(8, 14)]
    else:  # Monday to Friday
        return [f"{i:02d}:00" for i in range(8, 22)]

class DataManager:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)

    def save_appointment(self, appointment):
        filepath = os.path.join(self.data_dir, "zakazani_termini.csv")
        file_exists = os.path.isfile(filepath)
        
        with open(filepath, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Ime", "Prezime", "Broj", "Datum", "Vrijeme", "Zahvat"])
            writer.writerow([
                appointment.ime,
                appointment.prezime,
                appointment.broj,
                appointment.datum,
                appointment.vrijeme,
                appointment.zahvat
            ])

    def get_appointments(self):
        filepath = os.path.join(self.data_dir, "zakazani_termini.csv")
        if not os.path.isfile(filepath):
            return []
            
        try:
            with open(filepath, newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                return list(reader)
        except (FileNotFoundError, UnicodeDecodeError):
            return []

    def delete_appointment(self, appointment_to_delete):
        filepath = os.path.join(self.data_dir, "zakazani_termini.csv")
        appointments = self.get_appointments()
        
        # Filter out the appointment to delete
        filtered_appointments = [
            apt for apt in appointments 
            if not all([
                apt["Ime"] == appointment_to_delete.ime,
                apt["Prezime"] == appointment_to_delete.prezime,
                apt["Datum"] == appointment_to_delete.datum,
                apt["Vrijeme"] == appointment_to_delete.vrijeme
            ])
        ]

        try:
            with open(filepath, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["Ime", "Prezime", "Broj", "Datum", "Vrijeme", "Zahvat"])
                writer.writeheader()
                writer.writerows(filtered_appointments)
        except IOError:
            raise Exception("Greška pri brisanju termina") 
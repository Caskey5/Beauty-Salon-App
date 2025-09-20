# 💄 Beauty Salon Management System

A comprehensive desktop application for managing beauty salon operations, built with Python and Tkinter. This system provides a complete solution for appointment scheduling, user management, and salon administration.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## 🌟 Features

### 👤 User Management
- **Customer Registration**: Secure signup with password validation
- **Multi-role Authentication**: Admin, Employee, and Customer login
- **Profile Management**: User data storage and management

### 📅 Appointment System
- **Real-time Scheduling**: Interactive calendar with available time slots
- **Smart Availability**: Automatic detection of working hours and booked slots
- **Service Selection**: Choose from predefined beauty services with pricing
- **Appointment Management**: Book, view, and cancel appointments

### 👨‍💼 Admin Features
- **Employee Management**: Add and remove salon staff
- **Appointment Overview**: View all scheduled appointments
- **Service Administration**: Manage available services and pricing
- **Customer Management**: Access to customer information

### 💼 Employee Features
- **Customer Booking**: Schedule appointments for walk-in customers
- **Schedule Management**: View and manage daily appointments
- **Service Delivery**: Access to appointment details and customer information

### 🧾 Receipt System
- **Automatic Receipts**: Generate detailed receipts for completed services
- **File Storage**: Save receipts as text files for record keeping
- **Service Details**: Include service name, price, and appointment information

## 🏗️ System Architecture

```
Beauty-Salon-App/
├── components/          # UI Components
│   ├── login_frame.py   # Login interface
│   └── signup_frame.py  # Registration interface
├── models/              # Data Models
│   ├── appointment.py   # Appointment data structure
│   └── user.py          # User data structure
├── views/               # Dashboard Views
│   ├── admin_dashboard.py    # Admin interface
│   ├── employee_dashboard.py # Employee interface
│   └── user_dashboard.py     # Customer interface
├── utils/               # Utility Functions
│   └── data_manager.py  # Data management and CSV operations
├── validation/          # Input Validation
│   └── validators.py    # Password and data validation
├── data/                # Data Storage
│   ├── korisnici.csv    # Customer data
│   ├── zaposlenici.csv  # Employee data
│   ├── zakazani_termini.csv # Appointments
│   └── usluge.csv       # Services and pricing
├── pictures/            # Application Assets
│   └── pozadina.png     # Background image
├── računi/              # Generated Receipts
├── main.py              # Application entry point
└── requirements.txt     # Python dependencies
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/beauty-salon-app.git
cd beauty-salon-app
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python main.py
```

## 🔧 Dependencies

- **Pillow (10.0.0)**: Image processing and display
- **tkcalendar (1.6.1)**: Calendar widget for date selection
- **tkinter**: GUI framework (included with Python)
- **csv**: Data storage and management (built-in)
- **hashlib**: Password encryption (built-in)

## 📖 Usage Guide

### For Customers
1. **Registration**: Click "Sign up" and fill in your details
2. **Login**: Use your credentials to access your dashboard
3. **Book Appointment**: Select date, time, and service
4. **Manage Bookings**: View or cancel your appointments
5. **Get Receipt**: Print receipt after service completion

### For Employees
1. **Login**: Use employee credentials provided by admin
2. **Schedule Appointments**: Book appointments for walk-in customers
3. **View Schedule**: Check daily appointment schedule
4. **Manage Bookings**: Cancel or modify appointments as needed

### For Administrators
1. **Login**: Use admin credentials
2. **Staff Management**: Add or remove employees
3. **Service Management**: Update available services and pricing
4. **Appointment Overview**: Monitor all salon activities
5. **Reports**: Access customer and appointment data

## 🔐 Test Credentials

### Administrator Access
- **Username**: `Caskey`
- **Password**: `#Caskey123`

### Employee Access
- **Username**: `I1`
- **Password**: `#I1`

### Customer Access
- Register a new account using the "Sign up" feature
- Or use any existing customer credentials from the data files

## ⏰ Business Hours

- **Monday - Friday**: 08:00 - 21:00
- **Saturday**: 08:00 - 13:00
- **Sunday**: Closed

## 🛡️ Security Features

- **Password Hashing**: SHA-256 encryption for secure password storage
- **Input Validation**: Comprehensive validation for all user inputs
- **Role-based Access**: Different access levels for different user types
- **Data Integrity**: CSV-based storage with error handling

## 🔄 Data Management

### Data Storage
- All data is stored in CSV format for easy access and portability
- Automatic backup creation for data safety
- Unicode support for international characters

### File Structure
- `korisnici.csv`: Customer information and credentials
- `zaposlenici.csv`: Employee data and access credentials
- `zakazani_termini.csv`: All appointment records
- `usluge.csv`: Available services and pricing information

## 🎨 User Interface

- **Intuitive Design**: User-friendly interface with clear navigation
- **Responsive Layout**: Adaptive design for different screen sizes
- **Visual Feedback**: Clear confirmation messages and error handling
- **Accessibility**: Easy-to-read fonts and color schemes

## 🐛 Troubleshooting

### Common Issues

**Application won't start**
- Check if all dependencies are installed: `pip install -r requirements.txt`
- Ensure Python 3.8+ is installed: `python --version`

**Image not loading**
- Verify `pictures/pozadina.png` exists in the project directory
- Application will use fallback color if image is missing

**Data not saving**
- Check file permissions in the `data/` directory
- Ensure the application has write access to the project folder

**Calendar not working**
- Verify `tkcalendar` is properly installed
- Update to the latest version if needed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Caskey5**
- GitHub: [@Caskey5](https://https://github.com/Caskey5)
- Email: siljacantonio.biz@gmail.com

## 🙏 Acknowledgments

- Python community for excellent libraries
- Tkinter for the GUI framework
- All contributors and testers

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Caskey5/beauty-salon-app/issues) page
2. Create a new issue with detailed description
3. Contact the maintainer directly

---

**Made with ❤️ for beauty salon management**

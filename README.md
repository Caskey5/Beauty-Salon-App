# 💄 Beauty Salon Management System

A professional beauty salon management application built with **Clean Architecture** principles.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Architecture](https://img.shields.io/badge/architecture-Clean_Architecture-green.svg)
![Database](https://img.shields.io/badge/database-SQLite-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

---

## 🏗️ Architecture

This project follows **Clean Architecture** with clear separation of concerns across 5 layers:

```
beauty_salon/
├── main.py              # Application entry point (13 lines!)
├── di_container.py      # Dependency Injection Container
├── migrate_data.py      # Data migration tool
│
├── config/              # ⚙️ Configuration & Constants
│   ├── settings.py      # Application settings
│   └── constants.py     # Business constants
│
├── core/                # 🎯 Domain Layer (Business Logic)
│   ├── entities/        # Domain entities
│   ├── repositories/    # Repository interfaces
│   └── use_cases/       # Business use cases
│
├── data/                # 💾 Data Layer
│   ├── repositories/    # Repository implementations
│   │   └── sqlite/      # SQLite implementations
│   └── sources/         # Database files
│       └── salon.db     # SQLite database
│
├── infrastructure/      # 🔧 Infrastructure Layer
│   ├── database/        # Database connection & migrations
│   ├── security/        # Password hashing & validation
│   ├── file_handlers/   # Receipt generators
│   └── scheduling/      # Working hours service
│
├── presentation/        # 🎨 Presentation Layer (UI)
│   ├── application.py   # Main application class
│   ├── components/      # Login, Signup views
│   ├── dashboards/      # Admin, Customer, Employee dashboards
│   └── controllers/     # Application controller
│
├── assets/images/       # UI assets
└── receipts/            # Generated receipt files
```

---

## ✨ Features

### 👨‍💼 Admin Dashboard
- ✅ Add/remove employees
- ✅ Schedule appointments for customers
- ✅ Cancel appointments
- ✅ View all appointments
- ✅ Full salon management control

### 👤 Customer Dashboard
- ✅ Book personal appointments
- ✅ View own appointments
- ✅ Cancel appointments
- ✅ Generate receipts
- ✅ Self-service booking

### 👨‍🔧 Employee Dashboard
- ✅ Schedule appointments for walk-in customers
- ✅ View all salon appointments
- ✅ Cancel appointments
- ✅ Manage daily operations

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/beauty-salon-app.git
   cd beauty-salon-app
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the application**
   ```bash
   python main.py
   ```

---

## 🔑 Login Credentials

### 👨‍💼 Admin
- **Username:** `Caskey`
- **Password:** `#Caskey123`

**Admin capabilities:**
- Manage employees (add/remove)
- Book appointments for any customer
- View and cancel all appointments
- Full system access

### 👤 Customer
- Click **"Sign Up"** to create a new customer account
- Fill in: First Name, Last Name, Phone, Username, Password
- Password must meet security requirements

### 👨‍🔧 Employee
- Contact admin to create employee accounts
- Employees can book appointments and manage salon operations

---

## 📊 Database

The application uses **SQLite** for data persistence:

- **Location:** `data/sources/salon.db`
- **Tables:** `users`, `employees`, `appointments`, `services`
- **Auto-migration:** Database schema is created automatically on first run
- **Backup:** Simply copy the `salon.db` file

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.8+ |
| **GUI Framework** | Tkinter (built-in) |
| **Database** | SQLite3 (built-in) |
| **Architecture** | Clean Architecture |
| **Design Patterns** | DI, Repository, Use Case, MVC |
| **Security** | SHA-256 password hashing |
| **Dependencies** | Pillow, tkcalendar |

---

## 📦 Dependencies

```txt
Pillow>=10.0.0      # Image handling for background
tkcalendar>=1.6.1   # Calendar widget for date selection
```

> **Note:** `tkinter` and `sqlite3` come pre-installed with Python

**Install dependencies:**
```bash
pip install -r requirements.txt
```

---

## 🏢 Business Rules

### ⏰ Working Hours
| Day | Hours | Slots |
|-----|-------|-------|
| **Monday - Friday** | 08:00 - 21:00 | 13 hourly slots |
| **Saturday** | 08:00 - 13:00 | 5 hourly slots |
| **Sunday** | Closed | - |

### 💆 Available Services

| Service | Price |
|---------|-------|
| Eyelashes | 25€ |
| Manicure | 20€ |
| Physiotherapy | 35€ |
| Massage | 30€ |
| Facial Care | 28€ |
| Body Care | 32€ |
| Depilation | 15€ |
| Laser Depilation | 50€ |

### 🔒 Password Requirements
- ✅ Minimum 8 characters
- ✅ At least one uppercase letter
- ✅ At least one digit
- ✅ At least one special character (!@#$%^&*(),.?":{}|<>)

---

## 📁 Project Structure Details

### 🎯 Core Layer (Domain)
**Pure business logic - no dependencies on external frameworks**

```
core/
├── entities/         # Domain models (User, Employee, Appointment, Service)
├── repositories/     # Abstract repository interfaces (contracts)
└── use_cases/        # Business operations
    ├── auth/         # LoginUser, RegisterUser
    ├── appointments/ # CreateAppointment, CancelAppointment, GetAppointments
    ├── employees/    # AddEmployee, RemoveEmployee, GetEmployees
    └── services/     # GetServices
```

**Key principle:** The core never depends on infrastructure or presentation

### 💾 Data Layer
**Data access implementations**

```
data/
├── repositories/
│   └── sqlite/       # SQLite implementations of repository interfaces
└── sources/
    └── salon.db      # SQLite database file
```

### 🔧 Infrastructure Layer
**External concerns and utilities**

```
infrastructure/
├── database/         # Database connection & schema migrations
├── security/         # Password hashing (SHA-256) & validation
├── file_handlers/    # Receipt generation (TXT files)
└── scheduling/       # Working hours calculator
```

### 🎨 Presentation Layer
**User interface (Tkinter)**

```
presentation/
├── application.py    # Main application window and lifecycle
├── components/       # Reusable UI components (Login, Signup)
├── dashboards/       # Role-specific dashboards (Admin, Customer, Employee)
└── controllers/      # Navigation & state management
```

---

## 🔧 Development

### Architecture Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Testability** | Each layer can be tested independently |
| ✅ **Maintainability** | Changes in one layer don't affect others |
| ✅ **Scalability** | Easy to add new features |
| ✅ **Flexibility** | Easy to swap implementations (e.g., SQLite → PostgreSQL) |
| ✅ **Code Quality** | SOLID principles enforced |

### Adding New Features

1. **Add entity** in `core/entities/`
2. **Create repository interface** in `core/repositories/`
3. **Implement repository** in `data/repositories/sqlite/`
4. **Create use case** in `core/use_cases/`
5. **Wire dependencies** in `di_container.py`
6. **Create UI** in `presentation/`

### Code Standards

This project follows:
- ✅ **SOLID principles**
- ✅ **Clean Architecture**
- ✅ **Type hints** throughout
- ✅ **Docstrings** for all classes and methods
- ✅ **PEP 8** style guide
- ✅ **Separation of concerns**
- ✅ **Dependency injection**

---

## 🗃️ Data Migration

If you have old CSV data, migrate it to SQLite:

```bash
python migrate_data.py
```

**Migration process:**
1. ✅ Reads CSV files from `data/` directory
2. ✅ Creates database schema
3. ✅ Imports users, employees, and appointments
4. ✅ Seeds services automatically
5. ✅ Preserves password hashes

**Note:** Old CSV files can be deleted after successful migration

---

## 📄 Receipts

Customer receipts are generated as `.txt` files in the `receipts/` directory:

**Format:** `receipt_FirstName_LastName_Date.txt`

**Example:**
```
╔════════════════════════════════════════╗
║        BEAUTY SALON RECEIPT            ║
╚════════════════════════════════════════╝

Customer Information:
  Name: John Doe
  Phone: 1234567890

Appointment Details:
  Date: 2025-06-15
  Time: 10:00
  Service: Massage

Payment Information:
  Service Price: 30€

═══════════════════════════════════════════
Thank you for choosing our Beauty Salon!
```

---

## 🔒 Security

- ✅ **Password Hashing:** SHA-256 algorithm
- ✅ **No Plaintext Passwords:** All passwords stored as hashes
- ✅ **Input Validation:** All user inputs validated
- ✅ **SQL Injection Protection:** Parameterized queries
- ✅ **Role-Based Access:** Admin, Employee, Customer roles

---

## 📈 Project Metrics

| Metric | Value |
|--------|-------|
| **Python Files** | 60+ files |
| **Classes** | 40+ classes |
| **Lines of Code (main.py)** | 13 lines |
| **Architecture Layers** | 5 layers |
| **Design Patterns** | 4+ patterns |
| **Code Language** | 100% English |
| **Type Hints** | 100% coverage |
| **Documentation** | Comprehensive |

---

## 🤝 Contributing

This is an educational/portfolio project demonstrating Clean Architecture principles in Python.

**To contribute:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Follow the existing architecture patterns
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

---

## 📜 License

This project is for educational purposes.

---

## 👨‍💻 Author

Built with Clean Architecture principles following **Senior Python Developer** standards.

### Key Achievements
- ✅ **60+ Python files** organized in 5 layers
- ✅ **40+ classes** with single responsibility
- ✅ **100% English code** with comprehensive documentation
- ✅ **Type hints** throughout the codebase
- ✅ **Dependency Injection** for loose coupling
- ✅ **Repository Pattern** for data abstraction
- ✅ **Use Case Pattern** for business logic isolation

---

## 📚 Additional Resources

- [Clean Architecture by Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Repository Pattern](https://martinfowler.com/eaaCatalog/repository.html)
- [Dependency Injection](https://en.wikipedia.org/wiki/Dependency_injection)

---

**Built with ❤️ using Clean Architecture**

*Professional • Maintainable • Scalable*

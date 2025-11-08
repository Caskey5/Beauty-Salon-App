# Beauty Salon Management System

A professional beauty salon management application built with **Clean Architecture** principles.

## 🏗️ Architecture

This project follows **Clean Architecture** with clear separation of concerns:

```
beauty_salon/
├── config/              # Configuration & Constants
├── core/                # Domain Layer (Business Logic)
│   ├── entities/        # Domain entities
│   ├── repositories/    # Repository interfaces
│   └── use_cases/       # Business use cases
├── data/                # Data Layer
│   └── repositories/    # Repository implementations (SQLite)
├── infrastructure/      # Infrastructure Layer
│   ├── database/        # Database connection & migrations
│   ├── security/        # Password hashing & validation
│   ├── file_handlers/   # JSON & receipt generators
│   └── scheduling/      # Working hours service
├── presentation/        # Presentation Layer (UI)
│   ├── components/      # Login, Signup views
│   ├── dashboards/      # Admin, Customer, Employee dashboards
│   └── controllers/     # Application controller
└── di_container.py      # Dependency Injection Container
```

## ✨ Features

### 👨‍💼 Admin Dashboard
- Add/remove employees
- Schedule appointments for customers
- Cancel appointments
- View all appointments
- Full salon management control

### 👤 Customer Dashboard
- Book personal appointments
- View own appointments
- Cancel appointments
- Generate receipts
- Self-service booking

### 👨‍🔧 Employee Dashboard
- Schedule appointments for walk-in customers
- View all salon appointments
- Cancel appointments
- Manage daily operations

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   cd D:\Users\silja\Code\Repositories\Beauty-Salon-App
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migration** (optional if starting fresh)
   ```bash
   python migrate_data.py
   ```

4. **Start the application**
   ```bash
   python new_main.py
   ```

## 🔑 Login Credentials

### Admin
- **Username:** `Caskey`
- **Password:** `#Caskey123`

### Test Customer
- **Username:** `Lucija`
- **Password:** `Test123!`

### Test Employee
- **Username:** `Ivan`
- **Password:** `Test123!`

## 📊 Database

The application uses **SQLite** for data persistence:

- **Location:** `data/sources/salon.db`
- **Tables:** users, employees, appointments, services
- **Auto-migration:** Database schema is created automatically on first run

## 🛠️ Technology Stack

- **Language:** Python 3.8+
- **GUI:** Tkinter
- **Database:** SQLite3
- **Architecture:** Clean Architecture
- **Design Patterns:** Dependency Injection, Repository Pattern, Use Cases
- **Security:** SHA-256 password hashing

## 📦 Dependencies

```
Pillow>=10.0.0      # Image handling
tkcalendar>=1.6.1   # Calendar widget
```

## 🏢 Business Rules

### Working Hours
- **Monday - Friday:** 08:00 - 21:00
- **Saturday:** 08:00 - 13:00
- **Sunday:** Closed

### Services
1. Eyelashes - 25€
2. Manicure - 20€
3. Physiotherapy - 35€
4. Massage - 30€
5. Facial Care - 28€
6. Body Care - 32€
7. Depilation - 15€
8. Laser Depilation - 50€

### Password Requirements
- Minimum 8 characters
- At least one uppercase letter
- At least one digit
- At least one special character

## 📁 Project Structure Details

### Core Layer (Domain)
**Pure business logic - no dependencies on external frameworks**

- `entities/` - Domain models (User, Employee, Appointment, Service)
- `repositories/` - Abstract repository interfaces
- `use_cases/` - Business operations (LoginUser, CreateAppointment, etc.)

### Data Layer
**Data access implementations**

- `repositories/sqlite/` - SQLite implementations of repository interfaces

### Infrastructure Layer
**External concerns and utilities**

- `database/` - Database connection & migrations
- `security/` - Password hashing & validation
- `file_handlers/` - Receipt generation
- `scheduling/` - Working hours calculator

### Presentation Layer
**User interface**

- `components/` - Reusable UI components
- `dashboards/` - Role-specific dashboards
- `controllers/` - Navigation & state management

## 🔧 Development

### Running Tests
```bash
# Tests coming soon!
```

### Adding New Features

1. **Add entity** in `core/entities/`
2. **Create repository interface** in `core/repositories/`
3. **Implement repository** in `data/repositories/sqlite/`
4. **Create use case** in `core/use_cases/`
5. **Add to DI container** in `di_container.py`
6. **Create UI** in `presentation/`

## 📝 Code Quality

This project follows:
- **SOLID principles**
- **Clean Architecture**
- **Type hints** throughout
- **Docstrings** for all classes and methods
- **Separation of concerns**
- **Dependency injection**

## 🗃️ Data Migration

To migrate data from old CSV format to SQLite:

```bash
python migrate_data.py
```

This will:
- Import users from `data/korisnici.csv`
- Import employees from `data/zaposlenici.csv`
- Import appointments from `data/zakazani_termini.csv`
- Seed services automatically

## 📄 Receipts

Receipts are generated as `.txt` files in the `receipts/` directory:
- Format: `receipt_FirstName_LastName_Date.txt`
- Contains: Customer info, appointment details, service & price

## 🤝 Contributing

This is a educational/portfolio project demonstrating Clean Architecture principles in Python.

## 📜 License

This project is for educational purposes.

## 👨‍💻 Author

Built with Clean Architecture principles by a Senior Python Developer approach.

---

**Note:** This is a refactored version of the original application, now following enterprise-level Clean Architecture standards.

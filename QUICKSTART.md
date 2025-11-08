# 🚀 Quick Start Guide

## ✅ Installation Complete!

Your Beauty Salon application has been successfully refactored with **Clean Architecture**!

---

## 🏃 Running the Application

### Option 1: Run the new application
```bash
python new_main.py
```

### Option 2: Run tests
```bash
python test_app.py
```

### Option 3: Migrate old CSV data (if needed again)
```bash
python migrate_data.py
```

---

## 🔑 Login Credentials

### 👨‍💼 Admin Access
- **Username:** `Caskey`
- **Password:** `#Caskey123`

**Admin can:**
- Add/remove employees
- Schedule appointments for any customer
- Cancel any appointment
- View all appointments

### 👤 Customer Access (from migrated data)
- **Username:** `Lucija` or `Ivan`
- **Password:** (use the original passwords from your CSV)

**Note:** Customer passwords are hashed in database. If you don't remember them, you can:
1. Register a new customer via "Sign Up"
2. Or check the original CSV file: `data/korisnici.csv`

**Customers can:**
- Book their own appointments
- View their appointments
- Cancel their appointments
- Generate receipts

### 👨‍🔧 Employee Access (from migrated data)
- **Usernames:** `Lucija`, `Ivan`, `I1`, `Ivano`
- **Password:** (use the original passwords from your CSV)

**Note:** Check `data/zaposlenici.csv` for original credentials.

**Employees can:**
- Schedule appointments for walk-in customers
- View all appointments
- Cancel appointments

---

## 📊 Database Information

- **Type:** SQLite3
- **Location:** `D:\Users\silja\Code\Repositories\Beauty-Salon-App\data\sources\salon.db`
- **Status:** ✅ Initialized and migrated
- **Data:**
  - ✅ 2 users migrated
  - ✅ 4 employees migrated
  - ✅ 22 appointments migrated
  - ✅ 8 services seeded

---

## 🧪 Test Results

**All tests passed (5/5):**
- ✅ Database Connection & Schema
- ✅ Authentication System
- ✅ Data Retrieval
- ✅ Use Cases
- ✅ Appointment Creation

---

## 📁 Project Structure

```
beauty_salon/
├── new_main.py              # ⭐ START HERE - Main entry point
├── migrate_data.py          # Migration tool (CSV → SQLite)
├── test_app.py              # Test suite
│
├── config/                  # Configuration
├── core/                    # Business logic (entities, use cases)
├── data/                    # Data access layer (SQLite)
├── infrastructure/          # Cross-cutting concerns
└── presentation/            # UI layer (Tkinter)
```

---

## 🏢 Working Hours

- **Monday - Friday:** 08:00 - 21:00 (13 hourly slots)
- **Saturday:** 08:00 - 13:00 (5 hourly slots)
- **Sunday:** Closed

---

## 💰 Available Services

1. **Eyelashes** - 25€
2. **Manicure** - 20€
3. **Physiotherapy** - 35€
4. **Massage** - 30€
5. **Facial Care** - 28€
6. **Body Care** - 32€
7. **Depilation** - 15€
8. **Laser Depilation** - 50€

---

## 📝 Receipts

- Generated receipts are saved in: `receipts/`
- Format: `receipt_FirstName_LastName_Date.txt`

---

## 🔧 Troubleshooting

### "ModuleNotFoundError: No module named 'PIL'"
```bash
pip install Pillow tkcalendar
```

### "Database is locked"
- Close any other instances of the application
- Delete `salon.db` and run `migrate_data.py` again

### Can't login with old credentials
- Check `data/korisnici.csv` or `data/zaposlenici.csv` for usernames
- Passwords are hashed, so you may need to:
  - Register a new account
  - Or manually update the hash in the database

---

## 🎯 Next Steps

1. **Test the application:** Run `python new_main.py`
2. **Login as Admin:** Use `Caskey` / `#Caskey123`
3. **Explore the dashboards:** Try all features
4. **Create a test appointment:** Test the booking flow
5. **Generate a receipt:** Complete a booking and print receipt

---

## 📚 Full Documentation

See `README_NEW.md` for complete documentation including:
- Architecture details
- Development guide
- Code quality standards
- Contributing guidelines

---

## ✨ What Changed?

| Before | After |
|--------|-------|
| CSV files | SQLite database |
| Monolithic code | Clean Architecture (60+ files) |
| Mixed languages | 100% English code |
| No separation | 5 distinct layers |
| Hard to test | Fully testable |
| ~300 line main | 13 line main |

---

## 🎉 Enjoy Your Professional Beauty Salon App!

Built with ❤️ using Clean Architecture principles.

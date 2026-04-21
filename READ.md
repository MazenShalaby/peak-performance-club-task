# 🏋️ Gym Management System (Django)

This project is a Django-based Gym Management System that models core gym operations such as members, trainers, classes, branches, and equipment. It also includes custom business logic, query optimizations, and an enhanced Django admin interface.

---

## 📦 Models Overview

### 🔹 Base Model
**CreatedUpdatedTimeStamp**
- Abstract model used across all models.
- Automatically tracks:
  - `created_at`
  - `updated_at`

---

### 🔹 Member
- Stores:
  - `name`
  - `balance`
- Features:
  - `is_vip` property → Returns `True` if balance > 1000.

---

### 🔹 Trainer
- Stores:
  - `name`
  - `specialization`

---

### 🔹 Branch
- Stores:
  - `name`
  - `location`

---

### 🔹 GymClass
- Stores:
  - `title`
  - `base_price`
  - `start_date`
- Relationships:
  - `ForeignKey` → Trainer
  - `ManyToMany` → Members

#### Features:
- **Custom Manager & QuerySet**
  - `trending()` → Returns classes with high member enrollment.

- **Discount Logic**
  - `apply_discount(percentage=20)`
    - Applies a discount if the class is within a valid 30-day window.
    - Raises an error if the discount period has expired.

---

### 🔹 Equipment
- Stores:
  - `name`
  - `is_damaged`
- Relationships:
  - `ManyToMany` → Branch

---

## ⚙️ Advanced Querying

### Custom QuerySets & Managers

#### GymClass
- Custom QuerySet to:
  - Annotate number of members.
  - Filter trending classes.

#### Damaged Equipment
- Custom QuerySet to filter:
  - Only equipment where `is_damaged = True`.

---

## 🧩 Proxy Model

### DamagedEquipment
- Proxy model for `Equipment`.
- Does NOT create a new database table.
- Uses a custom manager to return only damaged items.
- Improves code readability and separation of concerns.

---

## 🛠️ Django Admin Customization

All models are registered with customized admin views:

### Features:
- `list_display` → Clean table view
- `search_fields` → Quick search
- `list_filter` → Easy filtering

### Special Setup:
- Separate admin views for:
  - **Equipment** → All items
  - **DamagedEquipment** → Only damaged items (via proxy model)

---

## 🚀 Key Highlights

- Reusable abstract base model for timestamps.
- Business logic inside models (clean architecture).
- Custom QuerySets & Managers for scalable querying.
- Proxy model usage for advanced filtering without extra tables.
- Fully customized Django admin interface.

---

## 📌 Notes

- The project follows Django best practices:
  - Fat models, thin views approach.
  - Separation of concerns using managers and querysets.
  - Clean and maintainable admin configurations.

---

## 📁 Tech Stack

- Python
- Django
- SQLite (default, can be replaced)

---

## 🧠 Future Improvements

- Add APIs (Django REST Framework)
- Add authentication & permissions
- Booking system for classes
- Payment integration
- Reporting dashboard

---

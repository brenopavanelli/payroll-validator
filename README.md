# 🧾 Payroll Audit System

**Automated payroll auditing tool that handles multiple calculation types, detects inconsistencies, and validates employee payment data.**

This project was designed for administrative use within public payroll management but also built with clean architecture and design patterns to serve as a portfolio project for software engineering positions.

---

## 🧠 Overview

The **Payroll Audit System** processes payroll spreadsheets (`.csv`) and generates validated, formatted reports (`.xlsx`).  
Each module can perform a different type of payroll validation (e.g., **Permanence Bonus**, **Hazard Pay**, **Overtime**, etc.), following the same architecture.

The system identifies inconsistencies between calculated values and the values provided by payroll systems, ensuring data accuracy and transparency.

---

## 🏗️ Architecture

This project follows a **modular architecture** combined with the **Template Method Design Pattern** to ensure scalability and maintainability.

### 🔹 Main concepts
- **Abstract base processor** defines the general workflow for payroll validation.
- **Concrete processors** (e.g., `PermanenceBonusProcessor`) implement the specific calculation rules.
- **Data handling layer** uses `pandas` for efficient CSV and XLSX operations.
- **Report generator** produces formatted `.xlsx` outputs, ready for audit or administrative review.
- **Clean folder structure** designed for future expansion (additional calculation modules).


---

## 🧩 Design Pattern: Template Method

The **Template Method** defines the skeleton of the payroll processing algorithm in a base class (`BaseProcessor`) while allowing subclasses to override specific steps.




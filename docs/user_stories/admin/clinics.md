# Clinic View (Admin Panel)

---

## User Story: View Clinics

### As an
Administrator with "clinics" access level

### I want to
View clinic details, employees, and branches

### So that
I can understand the full structure and setup of each clinic in the system

---

## Description

Users with `clinics` access can view all clinics in a **read-only** mode.

### Table View:
Displayed columns include:
- Clinic name
- Logo
- Address
- Timezone
- Owner

Each clinic row links to a **detailed view** with multiple tabs:
- `Info`
- `Employees`
- `Branches`

---

## Tab: Info
Displays general information about the clinic:
- Clinic `name`
- `logo`
- `address` (full)
- `country`
- `timezone`
- `currency`
- Owner info (name, email, etc.)

---

## Tab: Employees
Displays all employees assigned to the clinic.

### Table Columns:
- Full name
- Email
- Phone number
- Birthday
- Sex
- Color

### Detail View:
When clicking on an employee, the following fields are shown:
- First name
- Last name
- Email
- Phone number
- Birthday
- Sex
- Language
- Timezone
- Color
- Roles
- Branches

All fields are **read-only**.

---

## Tab: Branches
Displays all branches belonging to the selected clinic.

### Table Columns:
- Branch name
- Address

### Detail View:
Includes:
- All branch info (name, address, timezone, etc.)
- Current working schedule
- Current active price list

All information is **read-only**.

---

## Acceptance Criteria

- [ ] Administrators with `clinics` access can view a table of clinics.
- [ ] The table includes name, logo, address, timezone, and owner.
- [ ] Detail page includes 3 tabs: Info, Employees, Branches.
- [ ] Info tab displays all general clinic data and owner.
- [ ] Employees tab displays a table and detail view per employee (read-only).
- [ ] Branches tab displays a table and detail view per branch, including schedule and price list (read-only).

---

## Business Value

- Allows centralized administrative oversight into clinic structures.
- Ensures transparency across clinic staff, locations, and operational settings.
- Preserves data integrity by enforcing view-only access.


# Patient Profile

---

## User Story: View Patient List

### As an
Employee

### I want to
View a list of all patients in the system

### So that
I can quickly access their contact and demographic information

---

## Description

All employees can view the list of patients.
Each patient row displays:
- Full name
- Birthday
- Sex
- Email
- Phone number
- Birthday

---

## Acceptance Criteria

- [ ] Any employee can access the patient list.
- [ ] Each patient row includes full name, birthday, sex, email, and phone.

---

## User Story: View Patient Profile Tabs

### As an
Employee

### I want to
Access detailed patient information organized in tabs

### So that
I can see medical and contact data in a structured, clear way

---

## Description

Each patient profile includes three tabs:

### 1. General Info
- First name
- Last name
- Birthday
- Sex
- Email
- Phone number
- Birthday

### 2. Extra Contacts
- List of emergency contacts with:
  - First name + Last name
  - Relation (from directory)
  - Email
  - Phone number
  - Primary contact marker (toggleable, auto-set if no contacts exist)

### 3. Allergies
- List of allergies with:
  - Allergy type (FK to directory)
  - Allergy cause (FK to directory)
  - Allergy reaction (FK to directory)
  - Notes
  - Severity (enum)

---

## Acceptance Criteria

- [ ] All employees can view patient profiles and switch between tabs.
- [ ] Each tab loads data independently.
- [ ] All information is read-only unless the user has admin permissions.

---

## User Story: Edit Patient Profile (Tab-Based)

### As an
Administrator

### I want to
Edit patient information per tab

### So that
I can keep patient records accurate and up to date

---

## Description

Only users with the `administrator` role can edit patient information.
Each tab is edited independently.

### General Info tab:
- All fields are editable.

### Extra Contacts tab:
- Full CRUD (add, edit, delete contacts)
- Fields:
  - First name
  - Last name
  - Email
  - Phone number
  - Relation (FK)
  - `is_primary` is auto-assigned if no other contacts exist.
  - `is_primary` can be manually toggled via a button next to the contact.

### Allergies tab:
- Full CRUD on allergy entries
- Fields:
  - Allergy type (FK)
  - Allergy cause (FK)
  - Allergy reaction (FK)
  - Notes
  - Severity (enum)

---

## Acceptance Criteria

- [ ] Only administrators can edit patient profile tabs.
- [ ] Each tab supports editing independently.
- [ ] Extra contacts and allergies support full CRUD.
- [ ] `is_primary` is auto-set if no other contacts exist.
- [ ] `is_primary` can be toggled manually via button.

---

## Business Value

- Ensures complete and structured patient data management.
- Allows granular, role-based editing.
- Supports clinical safety and emergency access.


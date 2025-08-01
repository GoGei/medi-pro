# Cancelled Appointments

---

## User Story: View Cancelled Appointments

### As a
Clinic Employee or Owner

### I want to
Access a list of cancelled appointments

### So that
I can review which appointments were cancelled, by whom, and why

---

## Description

All appointments with status `cancelled` are displayed on a **dedicated page**, accessible via a link or button from the calendar view.

### Display behavior:
- Appointments are shown in a **scrollable list**, grouped by **date** of the original appointment.
- Each item displays:
  - `patient` name
  - `employee` (doctor or staff assigned)
  - `reason` for cancellation (predefined category)
  - `comment` (optional text field for explanation)

### Access:
- The cancelled appointments list is **visible to all users**.
- The list is **read-only**.

---

## Acceptance Criteria

- [ ] A dedicated page shows all appointments with status `cancelled`.
- [ ] Appointments are grouped by original appointment date.
- [ ] Each appointment displays patient, employee, reason, and comment.
- [ ] Page is accessible from the calendar view.
- [ ] The list is read-only and visible to all users.

---

## Business Value

- Improves transparency by tracking cancelled sessions.
- Allows staff to analyze frequency and reasons for cancellations.
- Maintains separation from active scheduling for clarity.


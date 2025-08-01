# Appointment Creation

---

## User Story: Create Appointment

### As an
Administrator

### I want to
Schedule an appointment for a patient with a specific employee in a branch

### So that
The patient is booked for a session and receives proper confirmation

---

## Description

Only users with the role **Administrator** can create new appointments.

### Appointment creation involves:
- Selecting a `patient`
- Selecting an `employee`
- Selecting a `branch`
- Selecting a `slot` (single time slot only)

### Slot generation:
- Available slots are **generated manually** by clicking a **"Generate Slots for a Week"** button.
- Only one slot can be selected per appointment.

### After creation:
- The appointment is created with status **`new`**.
- The `patient` receives an **email notification** with the appointment details.

---

## Acceptance Criteria

- [ ] Only users with the role `Administrator` can access the appointment creation form.
- [ ] The form includes fields for patient, employee, branch, and available slots.
- [ ] Slots are generated for a week using a button.
- [ ] Only one slot can be selected for each appointment.
- [ ] On submission, appointment status is set to `new`.
- [ ] Patient receives an email with appointment information after creation.

---

## Business Value

- Enables structured and role-restricted scheduling for clinic visits.
- Reduces double booking by enforcing single-slot selection.
- Notifies patients automatically, ensuring communication and preparedness.


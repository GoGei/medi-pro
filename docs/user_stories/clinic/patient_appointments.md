# Patient Appointment Flow

---

## User Story: Create Patient During Appointment Scheduling

### As an
Administrator

### I want to
Quickly register a new patient while creating an appointment

### So that
I can schedule visits for new patients without leaving the appointment flow

---

## Description

While creating an appointment, the administrator can click a **“+” button** next to the patient selection field. This opens a secondary modal for quick patient registration.

### Required fields in the patient form:
- `first_name`
- `last_name`
- `sex`
- `birthday`
- `email`
- `phone_number`

### Behavior:
- The patient form appears in a **modal overlay**.
- After successful form submission, the modal closes.
- The user is returned to the **appointment creation modal**, where the newly created patient is now selectable.

---

## Acceptance Criteria

- [ ] Only administrators can access the patient creation feature.
- [ ] Clicking the “+” opens a modal form with all required fields.
- [ ] All fields are validated before submission.
- [ ] After saving, the new patient is immediately available in the appointment form.
- [ ] The interface returns the user to the original appointment modal without losing progress.

---

## Business Value

- Streamlines the appointment process for new patients.
- Reduces context switching and increases scheduling efficiency.
- Ensures all necessary patient data is collected during intake.


# Calendar View

---

## User Story: View and Manage Appointments in Calendar

### As a
Clinic Employee or Owner

### I want to
View appointments in a calendar format

### So that
I can easily understand scheduling and availability by day and week

---

## Description

The calendar displays appointments with the following behavior:

### Appointment visibility:
- Only appointments with status `new` or `done` are shown.
- Appointments with status `cancelled` are excluded from the calendar and shown on a **separate page**.

### View modes:
- **Week view**: Displays appointments for **all doctors** from **Monday to Sunday**.
- **Day view**: Each column represents a **separate doctor**, showing their appointments for the selected day.

### UI behavior:
- Time slots that are **outside of working hours** (defined by both `branch` and `employee`) are **shaded in grey**.
- Calendar includes two filters:
  - `branch` filter
  - `employee` filter

- A button labeled **Add** opens a modal or popup for **adding a new appointment**.

---

## Acceptance Criteria

- [ ] Appointments with status `new` and `done` are displayed in the calendar.
- [ ] Appointments with status `cancelled` are not shown in the calendar view.
- [ ] Calendar has two modes: Day and Week.
- [ ] Week view shows appointments for all doctors (Mon–Sun).
- [ ] Day view shows separate columns per doctor for the selected date.
- [ ] Non-working hours are visually greyed out based on branch and employee settings.
- [ ] Calendar supports filtering by branch and employee.
- [ ] Clicking the **Add** button opens a form/modal to create a new appointment.

---

## Business Value

- Provides intuitive visual scheduling for clinic operations.
- Prevents double-booking and off-hours scheduling.
- Enables quick filtering by staff and location.
- Separates cancelled appointments to avoid clutter and confusion.


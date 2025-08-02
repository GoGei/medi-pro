# Employee Schedule Management

---

## User Story: View Employee Schedule

### As an
Employee, Administrator, or Owner

### I want to
View the working schedule of an employee across time periods

### So that
I can understand when and where the employee is available to work

---

## Description

Each employee has one or more schedule periods, represented as date ranges. The schedule page displays these as **tabs**:
- Example: `1 Aug – 6 Sep 25` | `7 Sep 25 – 8 Apr 26` | ...

Upon selecting a tab, the corresponding schedule is shown as a **day-by-day breakdown**, where each day can include multiple time blocks across branches.

Example format:
```
Monday:
  - Branch A: 08:00–13:00
  - Branch B: 13:00–18:00
```

---

## Acceptance Criteria

- [ ] All users can view employee schedules.
- [ ] Schedules are grouped into tabs by date ranges.
- [ ] Each tab displays a weekly schedule broken down by day and branch.
- [ ] Multiple time blocks per day are allowed across different branches.

---

## User Story: Edit Employee Schedule

### As an
Owner, Administrator, or the Employee (editing own schedule)

### I want to
Edit the weekly work schedule for an employee

### So that
It reflects real branch assignments and working hours

---

## Description

Authorized users can modify an employee's weekly schedule within a selected period.

### UI Behavior:
- Days of the week are toggleable (on/off).
- Inside each day, user can:
  - Add time blocks with:
    - `branch`
    - `start_time`
    - `end_time`
  - Delete blocks (via trash icon)
- Time blocks for a day must not overlap.
- Blocks may follow sequentially (e.g., 08:00–13:00 at Branch A, then 13:00–18:00 at Branch B)

### Save Logic:
- All changes are saved only when clicking **Save**.
- Deleting a block is disallowed if that block includes appointments in the future.

---

## Acceptance Criteria

- [ ] Only owners, administrators, or the employee themselves can edit the schedule.
- [ ] Schedule is divided by day, with support for multiple branches per day.
- [ ] Users can add blocks with `+` and delete them with the trash icon.
- [ ] Start and end times must not overlap within the same day.
- [ ] Days can be toggled on or off.
- [ ] Changes are saved only after clicking **Save**.
- [ ] Attempting to delete a block that contains appointments results in an error.

---

## Business Value

- Enables dynamic, multi-branch scheduling for flexible staff planning.
- Prevents conflicts and maintains scheduling integrity.
- Allows self-management by employees while maintaining control by clinic leads.
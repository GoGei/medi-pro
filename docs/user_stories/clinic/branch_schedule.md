# Branch Schedule Management

---

## User Story: View Branch Schedule

### As an
Employee

### I want to
See the working schedule of a branch

### So that
I know the general availability of the clinic for appointments

---

## Description

Each branch has a schedule consisting of working hours for each day of the week.

- The schedule is displayed as a list:
  - Monday: 08:00–17:00
  - Tuesday: 08:00–17:00
  - ...

All employees can view this information.

---

## Acceptance Criteria

- [ ] Any employee can view the branch schedule.
- [ ] Schedule is shown as a day-by-day list with start and end times.

---

## User Story: Edit Branch Schedule

### As an
Administrator or Owner

### I want to
Edit the weekly working hours for a branch

### So that
I can maintain accurate operating times for appointment scheduling

---

## Description

Users with the role `owner` or `administrator` can edit a branch's weekly schedule.

### UI Behavior:
- Days of the week are presented as toggleable items.
- For each active day, the user selects:
  - Start time (via time selector)
  - End time (via time selector)
- Validation: `start_time` must be earlier than `end_time`

### Save Logic:
- After saving, the new schedule becomes active **starting tomorrow**.
- The previous schedule is automatically closed **with today's date**.

### Restrictions:
- At least **one working day** must be selected to save.
- If saving would result in **future `new` appointments** falling outside the new schedule, the action is blocked with an error.

---

## Acceptance Criteria

- [ ] Only administrators and owners can access edit mode.
- [ ] Editing interface includes toggle per day and time selectors.
- [ ] Start time must be earlier than end time for each day.
- [ ] At least one working day must be selected to proceed.
- [ ] Saving applies the new schedule starting tomorrow.
- [ ] Existing schedule is closed as of today.
- [ ] If future appointments conflict with the new schedule, saving is prevented and an error is shown.

---

## Business Value

- Ensures accurate and dynamic control over clinic working hours.
- Prevents scheduling conflicts or gaps in operating time.
- Maintains historical consistency by versioning previous schedules.


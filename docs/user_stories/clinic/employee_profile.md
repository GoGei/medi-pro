# Employee Profile Management

---

## User Story: Edit My Profile

### As an
Employee

### I want to
Edit my personal and work-related information

### So that
My profile is accurate and reflects my preferences and assignments

---

## Description

All employees can access and update their **own profile** via the profile screen.

### Editable fields:
- `first_name`
- `last_name`
- `birthday`
- `sex`
- `branches` (multiple selection from available branches)
- `timezone` (selection from predefined list)
- `color` (selection from color directory)

### Read-only fields:
- `email`
- `role`

Changes are saved via a **Save** button.
All changes are applied only after confirmation.

---

## Acceptance Criteria

- [ ] Any employee can access and edit their own profile.
- [ ] Only editable fields are modifiable; read-only fields are locked.
- [ ] The list of available branches, timezones, and colors is loaded from directories.
- [ ] Changes are saved only after confirmation via Save.
- [ ] Email and role are always visible but cannot be changed by the user.

---

## Business Value

- Empowers users to manage their own data without administrative involvement.
- Ensures profile consistency for features that depend on personal or regional data.
- Prevents accidental or unauthorized changes to critical identity fields.


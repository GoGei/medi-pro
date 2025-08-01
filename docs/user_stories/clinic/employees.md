# Employee View and Edit

---

## User Story: View Employee Profile

### As an
Employee

### I want to
See the details of any other employee in the clinic

### So that
I can understand who they are and what role they hold

---

## Description

Any logged-in user can view the profile of any employee.

Displayed fields:
- First name
- Last name
- Birthday
- Sex
- Email
- Role
- Branches
- Timezone
- Color

---

## Acceptance Criteria

- [ ] Any user can view any employee’s profile.
- [ ] All profile fields are shown in read-only mode for users without edit permissions.

---

## User Story: Edit Employee Profile

### As an
Owner or Administrator

### I want to
Edit employee details

### So that
I can maintain up-to-date and accurate staff information

---

## Description

Users with the role `owner` or `administrator` can edit employee profiles.

### Editable fields for both roles:
- First name
- Last name
- Birthday
- Sex
- Branches
- Timezone
- Color

### Role editing:
- Only users with the `owner` role can modify an employee’s `role` field.
- An `owner` cannot change **their own** role to anything other than `owner`.

---

## Acceptance Criteria

- [ ] Only owners and administrators can access edit mode.
- [ ] All editable fields are enabled for users with access.
- [ ] Role can only be changed by users with `owner` role.
- [ ] An owner cannot change their own role.

---

## Business Value

- Allows for role-restricted employee management.
- Maintains clear visibility of staff structure and responsibilities.
- Protects against accidental privilege loss for high-level users.


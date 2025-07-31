# Employee Invitation

---

## User Story: View Employee List

### As an
Employee

### I want to
See a list of all employees in my clinic

### So that
I can understand who works in the clinic and what roles they have

---

## Description

All employees, regardless of their role, can access and view the list of employees in the system.

Each entry includes:
- First and last name
- Email
- Role
- Status (e.g. active, not invited, invitation sent, etc.)
- Assigned branches

---

## Acceptance Criteria

- [ ] Any employee can view the employee list.
- [ ] Each employee displays basic info and assigned branches.
- [ ] Access is read-only unless the user has permission to invite or edit.

---

## User Story: Invite New Employee

### As an
Owner or Administrator

### I want to
Invite a new employee to the system

### So that
They can access the platform and start working with the clinic

---

## Description

Users with the `owner` or `administrator` role can invite new employees via an invitation form.

### Fields in the form:
- `email` *(required)*
- `first_name` *(required)*
- `last_name` *(required)*
- `birthday` *(required)*
- `sex` *(required)*
- `phone_number` *(required)*
- `branches` *(required, multiple allowed)*
- `invite_immediately` *(optional checkbox)*

### Invitation behavior:
- If **invite_immediately** is checked:
  - An invitation email is sent right after submission.
  - The employee receives **status: invitation_sent**.
- If **invite_immediately** is unchecked:
  - The employee is created with **status: not_invited**.
- An invitation link is valid for **1 day**.
- After expiration, the invitation is marked as **expired**.
- Invitation links can be re-sent, but not more than once per **5 minutes**.
- Only the **latest link** is active; previous links are invalidated.

---

## Acceptance Criteria

- [ ] Only users with `owner` or `administrator` role can invite employees.
- [ ] The invite form includes all required fields.
- [ ] Submitting with `invite_immediately` sends the invitation and updates status.
- [ ] Without `invite_immediately`, employee is created with status `not_invited`.
- [ ] A user cannot resend invite more than once every 5 minutes.
- [ ] Invitation link expires after 1 day.
- [ ] Only the most recent invite link is active.

---

## Business Value

- Enables secure onboarding of new staff into the clinic system.
- Ensures control over invitation lifetimes and access validity.
- Supports both immediate and delayed invitations for flexible workflow.
- Prevents abuse through link expiration and rate limiting.

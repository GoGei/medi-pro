# Administrator Management (Admin Panel)

---

## User Story: View Administrators

### As an
Administrator with "view" access level

### I want to
See a list and details of all system administrators

### So that
I can monitor who has administrative access and their roles

---

## Description

Users with "view" permission for administrators can:
- Access a table listing all administrator accounts
- Customize which columns are visible in the table
- Access a detailed view page for each administrator

The table displays:
- Email
- First name
- Last name
- `is_staff` status
- `is_superuser` status

Action buttons (based on permissions):
- **Edit** – visible if user has "change" access
- **Reset Password** – visible only for `superuser`

The detail page includes:
- Full administrator profile fields
- Buttons: `Back to list`, `Edit`, `Reset Password`
- If the user is viewing their own profile, a `Change Password` button is also available

---

## Acceptance Criteria

- [ ] Table of administrators is available to users with "view" access
- [ ] Users can configure column visibility in the table
- [ ] Each administrator can be opened in a detailed view
- [ ] `Edit` button is visible to users with "change" access
- [ ] `Reset Password` button is only visible to superusers
- [ ] `Change Password` button is shown only when viewing own profile

---

## User Story: Add Administrator

### As an
Administrator with "add" access level

### I want to
Create a new administrator with appropriate privileges

### So that
They can access and manage administrative parts of the system

---

## Description

Users with "add" access can add new administrator accounts via a form:

### Fields:
- `email`
- `first_name`
- `last_name`
- `is_staff` (toggle)
- `is_superuser` (toggle)

Behavior:
- By default, `is_superuser` field is disabled and turned off
- If the current user **is a superuser**, the field is **enabled**, but still **off by default**

After submitting the creation form, the user is redirected to a **password setup page**.

### Password Page:
- Required fields:
  - `password`
  - `confirm_password`

Validation rules:
- Password must include at least:
  - one lowercase letter
  - one uppercase letter
  - one digit
  - one special character from `!@#$%^&*()`
- Passwords must match

After setting the password, the user is redirected to the **detail view** of the newly created administrator.

---

## Acceptance Criteria

- [ ] Users with "add" access can open the add administrator form
- [ ] `is_superuser` is disabled unless the current user is a superuser
- [ ] After creating the admin, user is redirected to password setup page
- [ ] Password page enforces all listed validation rules
- [ ] After setting the password, user is redirected to the admin's detail page

---

## User Story: Edit Administrator

### As an
Administrator with "change" access level

### I want to
Edit administrator details (excluding password)

### So that
I can update their names, statuses, and permissions

---

## Description

Users with "change" permission can access an edit form with the same fields as creation (except password fields).

After saving, the user is redirected to the detail view of the administrator.

---

## Acceptance Criteria

- [ ] Users with "change" access can edit administrator details
- [ ] `is_superuser` toggle is editable only by superusers
- [ ] After saving, user is redirected to the administrator’s detail page

---

## Business Value

- Enables secure and role-controlled administrative access
- Ensures clear distinction between viewing, editing, and password-reset capabilities
- Protects superuser roles by restricting sensitive operations


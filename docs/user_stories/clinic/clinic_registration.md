# User Story: Clinic Registration

## Title
Clinic Owner Registration Flow

## As a
Clinic Owner

## I want to
Register a new clinic account on the platform

## So that
I can access the system and manage clinic-related operations

---

## Description

When a new user lands on the site, they are presented with a **login form by default**, which includes links to **register** a new account and **recover** a forgotten password.

Upon clicking the **register** link, the user is redirected to the **registration form**, where they must provide the following information:

- `clinic_name`
- `first_name`
- `last_name`
- `email` *(converted to lowercase before processing)*
- `country` (location of the clinic)
- `password`
- `confirm_password`
- Accept the **Terms of Use** (checkbox - required)

**Password Requirements:**
- At least one lowercase letter
- At least one uppercase letter
- At least one digit
- At least one special character: `!@#$%^&*()`

After submitting the form:

1. The system stores a **clinic request** linked to the lowercase email.
2. The provided email address becomes **blocked for 24 hours**, preventing duplicate registrations.
3. A confirmation email is sent to the user with a verification link.
4. A success message is shown instructing the user to **verify their email**.
5. Upon visiting the verification link:
    - The `clinic_request` is marked as verified.
    - A `clinic` instance is created automatically, along with any required associated models.
    - The user is allowed to log in.

If the email is **not verified within 24 hours**, the associated clinic request expires, and the email becomes eligible for registration again.

---

## Acceptance Criteria

- [ ] The default form on landing is **Login**, with links to **Register** and **Forgot Password**.
- [ ] Register form collects and validates all required fields.
- [ ] Email is saved and processed in lowercase.
- [ ] Password must include at least:
  - one lowercase letter
  - one uppercase letter
  - one digit
  - one special character from `!@#$%^&*()`
- [ ] Password and Confirm Password must match.
- [ ] Terms of Use checkbox must be checked to proceed.
- [ ] Submitting the form creates a **clinic request** and blocks the email for 24 hours.
- [ ] Confirmation email is sent immediately.
- [ ] User cannot register again with the same email within 24 hours unless verification fails or expires.
- [ ] User cannot register with already taken email (clinic is activated).
- [ ] Clicking the verification link creates the **clinic** instance and related models.
- [ ] Only verified users are allowed to log in.

---

## Business Value

- Enforces security by verifying email ownership.
- Ensures clean, lowercase, normalized email storage.
- Prevents abuse by blocking multiple attempts with the same email in a short period.
- Automatically bootstraps the system with a properly linked clinic and its data.

---

## Notes

- Login and Forgot Password flows will be documented separately.
- Email verification logic should automatically handle expiration and allow re-registration.
- Associated models created on verification may include default settings, permissions, or staff roles.

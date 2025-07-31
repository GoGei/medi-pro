# User Story: Employee Login

## Title
Login flow with optional 2FA and access restrictions

## As a
Clinic Owner or Employee

## I want to
Log in using my email and password

## So that
I can access the system and manage clinic operations

---

## Description

The user sees a login form with the following fields:

- `email`
- `password`

### Without 2FA enabled:
- After entering valid credentials, the user is immediately redirected to the **Home page**.

### With 2FA enabled:
- After submitting valid credentials, the user is redirected to a **2FA screen**, where they must enter a one-time code (OTP).
- If the correct code is entered, the user is granted access and redirected to the **Home page**.
- If the user **spends more than 3 minutes** on the 2FA screen **without completing verification**, they are **returned to the login screen** with the email + password form.

### Login protection:
- If a user enters a **wrong password 5 times in a row** for an existing email address, the system temporarily **blocks further login attempts for 5 minutes**.
- During this block period, even correct credentials will not grant access.

### Access restrictions:
Even with valid credentials and a successful 2FA (if enabled), the user will **not be allowed to log in** under the following conditions:

- The employee account is marked as **inactive** (e.g. soft-deleted or deactivated).
- The employee has been **terminated** from the organization.
- The account has not yet completed **email/account verification**.
- The clinic the user belongs to is marked as **inactive**.

---

## Acceptance Criteria

- [ ] Login form displays `email` and `password` fields.
- [ ] On valid credentials with no 2FA: user is redirected to **Home**.
- [ ] On valid credentials with 2FA: user is redirected to **OTP screen**.
- [ ] OTP screen allows user to input a code and proceed to Home if the code is correct.
- [ ] If the user does not enter the correct OTP within 3 minutes, they are returned to the login screen.
- [ ] If incorrect password is entered 5 times for a valid email, login is blocked for 5 minutes.
- [ ] A blocked user sees an appropriate error message and cannot proceed until time expires.
- [ ] User cannot log in if:
  - [ ] Their account is inactive or deleted
  - [ ] They are marked as terminated
  - [ ] Their account has not been verified
  - [ ] Their clinic is marked as inactive
- [ ] In all such cases, an appropriate error message is shown on the login screen.

---

## Business Value

- Supports secure login with optional two-factor authentication.
- Protects against brute-force attacks.
- Ensures only authorized and active users from valid clinics can access the system.
- Reinforces business rules around employment and account status.

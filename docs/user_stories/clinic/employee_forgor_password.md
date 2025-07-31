# User Story: Forgot Password

## Title
Password Recovery Flow

## As a
Clinic Owner or Employee

## I want to
Reset my password if I forget it

## So that
I can regain access to the system securely and continue working

---

## Description

On the login screen, the user can click on a **"Forgot password"** link.

1. The user is shown a form with a single field: `email`.
2. After entering a valid email, the system automatically sends a **password reset email**.
3. The user sees a success screen confirming that instructions have been sent.

Upon clicking the link in the email:

4. The user is redirected to a **Reset Password** form containing:
   - `new_password`
   - `confirm_password`

5. After entering a valid password and confirming it, the user is automatically redirected to the **Home page**.

### Password Requirements:
- At least one lowercase letter
- At least one uppercase letter
- At least one digit
- At least one special character: `!@#$%^&*()`

### Reset Link Behavior:
- The reset link is **valid for 1 hour** from the time of request.
- After the **first successful visit**, the link becomes **inactive**.
- If multiple reset emails were sent, **only the latest link remains active**. All previous links are invalidated.

---

## Acceptance Criteria

- [ ] A **"Forgot password"** link is visible on the login page.
- [ ] Clicking the link opens a form with an `email` field.
- [ ] Submitting the form with a valid email sends a password reset email.
- [ ] The user sees a success message after submitting the request.
- [ ] The reset email contains a secure, single-use link valid for 1 hour.
- [ ] Only the most recent reset link remains active if multiple were sent.
- [ ] Reset form includes `new_password` and `confirm_password`.
- [ ] Password must meet all complexity requirements.
- [ ] On successful reset, user is redirected to the **Home page**.
- [ ] Expired or already-used links display an appropriate error and deny access.

---

## Business Value

- Provides users a secure and fast way to recover access.
- Prevents misuse through time-limited, single-use links.
- Enforces strong password policies to maintain system integrity.

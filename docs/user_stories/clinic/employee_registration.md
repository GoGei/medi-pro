# Employee Registration

---

## User Story: Accept Invitation and Activate Account

### As an
Invited Employee

### I want to
Complete my profile and access the system

### So that
I can begin working with the clinic

---

## Description

After clicking the invitation link in the email:

1. The invitation status changes to **in_progress**.
2. The invited employee is shown a registration form with the following **editable fields**:
   - `first_name`
   - `last_name`
   - `birthday`
   - `sex`
   - `phone_number`

   Additionally, the form displays the following fields in **read-only** mode:
   - `email`
   - Assigned `branches` (from the clinic)

3. After submitting the form:
   - The employee is fully registered in the system.
   - The user is automatically logged in and redirected to the **Home page**.

4. If the form is **not completed within 1 hour**, the invitation becomes inactive and cannot be used again.

---

## Acceptance Criteria

- [ ] Clicking the invite link sets invitation status to `in_progress`.
- [ ] The registration form displays editable and read-only fields appropriately.
- [ ] All required fields must be filled before submission.
- [ ] After successful registration, the employee is redirected to the Home page.
- [ ] If 1 hour passes without submission, the invite link expires and cannot be reused.

---

## Business Value

- Ensures that only invited and verified users can activate access.
- Captures essential employee data required for clinic operations.
- Prevents unauthorized or delayed activation through time-bound registration.

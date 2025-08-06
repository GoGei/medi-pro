# Clinic Requests (Admin Panel)

---

## User Story: View Clinic Requests

### As an
Administrator with "clinicRequests" access level

### I want to
View and manage incoming clinic registration requests

### So that
I can monitor new clinic onboarding and trigger re-sending of activation emails

---

## Description

Administrators with the `clinicRequests` permission can access a **read-only** table of all clinic registration requests, including both **open** and **closed** ones (i.e., those already linked to created clinics).

### Table columns:
- Clinic name
- Owner full name
- Email
- Country
- Action buttons:
  - `View`
  - `Resend` (only for eligible requests)

### Detail View:
- Shows all available fields from the clinic request, including request status and timestamps.

### Restrictions:
- Clinic requests **cannot be edited**.
- The `Resend` button is only visible for requests in status:
  - `send`
  - `expired`

### Resend Behavior:
- Clicking `Resend` triggers a **new activation email** to the provided email address.
- Only available on eligible requests.

---

## Acceptance Criteria

- [ ] Users with `clinicRequests` access can see the full list of clinic requests.
- [ ] Both open and closed (linked to created clinics) requests are included.
- [ ] The table shows: clinic name, owner full name, email, country, and actions.
- [ ] `View` button opens a detail page with full request data.
- [ ] `Resend` button is visible only if request status is `send` or `expired`.
- [ ] Clicking `Resend` sends an activation email.
- [ ] No clinic request can be edited.

---

## Business Value

- Provides visibility into clinic registration pipeline.
- Allows recovery of stalled or expired registrations via controlled email resends.
- Maintains integrity by disallowing edits to original requests.


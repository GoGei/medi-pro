# Clinic Profile

---

## User Story: View Clinic Profile

### As an
Employee or Owner

### I want to
View the basic profile and configuration of the clinic

### So that
I can understand its identity and key settings

---

## Description

All users can access and view the clinic’s profile. The profile includes:
- Name
- Logo
- Address (City, Street, Apartment, ZIP code)
- Country
- Timezone
- Currency

The information is displayed in a clean, read-only format for general users.

---

## Acceptance Criteria

- [ ] Any user can view the clinic profile.
- [ ] All key fields (name, address, country, etc.) are displayed.

---

## User Story: Edit Clinic Profile

### As an
Owner

### I want to
Edit the clinic’s core settings

### So that
I can update the identity and system defaults of the clinic

---

## Description

Only users with the role `owner` can edit the clinic profile.

### Editable fields:
- `name`
- `logo`
- Address fields:
  - `city`
  - `street`
  - `apartment`
  - `zip_code`
- `country` (from directory)
- `timezone` (from directory)
- `currency` (from directory)

### Smart Defaults:
If the admin part includes preset configurations, suggestions for `timezone` and `currency` may be offered automatically based on the selected `country`.

---

## Acceptance Criteria

- [ ] Only the `owner` can edit clinic profile fields.
- [ ] All listed fields are editable.
- [ ] Timezone and currency suggestions are shown if presets exist for selected country.
- [ ] Changes are saved only after confirmation.

---

## Business Value

- Centralizes control over clinic configuration.
- Supports internationalization through dynamic defaults.
- Ensures a consistent and up-to-date profile for display and integrations.


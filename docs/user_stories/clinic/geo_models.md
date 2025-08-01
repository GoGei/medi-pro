# Geo Models

---

## User Story: Use Country and Timezone Selections

### As a
Clinic User (Employee or Owner)

### I want to
Select countries and timezones in relevant forms

### So that
I can provide accurate location and regional settings for myself or the clinic

---

## Description

The system includes the following geo-related reference models:
- `Country`
- `Timezone`

These models are not directly browsable in the UI, but are made available via **API endpoints** for use in dropdown fields throughout the application (e.g., employee profile, clinic registration, branch settings).

All users can:
- See the available countries and timezones as dropdowns in relevant forms.
- Use these values when filling or editing data.

Geo model values are **configured and managed exclusively from the administrative interface**.
User stories for admin management will be defined separately.

---

## Acceptance Criteria

- [ ] Country and Timezone dropdowns are available in forms where location or time context is required.
- [ ] The dropdown values are populated from system-wide geo reference models.
- [ ] These values are retrieved from API and always reflect current data.
- [ ] Users cannot browse or manage these lists in the clinic-facing UI.

---

## Business Value

- Enables consistent location and timezone selection across the system.
- Prevents errors by limiting inputs to predefined, validated values.
- Supports future internationalization and timezone-aware features.


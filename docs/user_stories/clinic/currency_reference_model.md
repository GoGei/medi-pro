# Currency Reference Model

---

## User Story: Use Currency Directory in Forms

### As a
Clinic User (Administrator or Owner)

### I want to
Select a valid currency from a predefined list

### So that
I can assign the correct financial context to the clinic or price-related settings

---

## Description

The system includes a reference model:
- `Currency`

This model defines supported currencies (e.g., USD, EUR, PLN, EGP) and is used wherever currency selection is required (e.g., in the clinic profile or pricing configuration).

It is not directly accessible in the clinic-facing UI but is made available via **API endpoints** to populate dropdown fields in relevant forms.

Currency values are **managed exclusively through the administrative interface**, ensuring global consistency across the system.

---

## Acceptance Criteria

- [ ] Currency dropdowns are available in all forms requiring currency selection.
- [ ] Values are loaded from the `Currency` reference model via API.
- [ ] Users cannot directly manage or browse the full currency list in the clinic-facing UI.
- [ ] Dropdowns reflect the current list managed from the admin panel.

---

## Business Value

- Standardizes financial inputs across clinics and countries.
- Prevents errors from inconsistent or invalid currency entries.
- Supports future billing logic, reporting, and localization.
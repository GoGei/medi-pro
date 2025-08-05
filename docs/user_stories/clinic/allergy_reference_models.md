# Allergy Reference Models

---

## User Story: Use Allergy Directory Models in Forms

### As a
Clinic User (Administrator or Employee)

### I want to
Select allergy-related values from predefined directories

### So that
I can record consistent and structured allergy data for patients

---

## Description

The system includes the following allergy-related reference models:
- `AllergyType`
- `AllergyCause`
- `AllergyReaction`

These models are not directly browsable in the UI, but are made available via **API endpoints** for use in dropdown fields throughout the application (e.g., patient allergy forms).

All users can:
- See available values for allergy type, cause, and reaction when entering patient allergy data.
- Use these values via dropdowns in forms.

These reference values are **configured and managed exclusively through the administrative interface**. Any updates are reflected automatically in all API-driven dropdowns.

---

## Acceptance Criteria

- [ ] AllergyType, AllergyCause, and AllergyReaction dropdowns are available in all relevant forms.
- [ ] The dropdowns are populated via API from reference models.
- [ ] These values are always up to date with admin-managed data.
- [ ] Users cannot browse or modify these models directly from the clinic interface.

---

## Business Value

- Ensures uniformity and accuracy in allergy records.
- Reduces manual input errors by limiting values to controlled lists.
- Supports future integration with clinical decision support or analytics.
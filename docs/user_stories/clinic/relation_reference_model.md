# Relation Reference Model

---

## User Story: Use Relation Directory in Forms

### As a
Clinic User (Administrator or Employee)

### I want to
Select predefined relationship types for a patient's emergency contacts

### So that
I can accurately describe the relation between the patient and their extra contacts

---

## Description

The system includes a reference model:
- `Relation`

This model defines possible relationship types for **extra contacts** (e.g., Mother, Father, Guardian, Spouse, etc.).

It is not directly browsable in the clinic-facing UI, but is exposed via **API endpoints** for use in dropdown fields within forms related to patient emergency contacts.

All users can:
- Select a relation value from the list when adding or editing an extra contact.

This directory is **configured and maintained only via the administrative interface**, ensuring consistency.

---

## Acceptance Criteria

- [ ] A dropdown for selecting relation is available in the extra contact form.
- [ ] The values are loaded from the Relation reference model via API.
- [ ] The dropdown always reflects the current admin-managed list.
- [ ] Clinic users cannot edit or browse the full relation list directly.

---

## Business Value

- Standardizes relationship descriptions for emergency contacts.
- Reduces input variability and confusion in contact records.
- Lays foundation for consistent reporting and integration.


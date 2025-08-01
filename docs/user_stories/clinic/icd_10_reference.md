# ICD-10 Reference

---

## User Story: View ICD-10 List

### As a
Clinic Employee or Owner

### I want to
Access a full list of ICD-10 codes with their names

### So that
I can reference medical codes while working with services or diagnoses

---

## Description

All users in the system can access the **ICD-10 reference**, which is presented as a large, searchable table containing:

- `code` (e.g., A00, B20)
- `name` (ICD-10 description/title)
- `last_updated` timestamp (visible to all users)

The table supports:
- Scrolling and pagination for performance
- Search/filter by code or name
- Read-only access for all users

The **ICD-10 list is updated manually** from the administrative side of the system.
User stories for managing updates will be added separately.

---

## Acceptance Criteria

- [ ] Any logged-in user can access the ICD-10 reference.
- [ ] The table displays `code`, `name`, and `last_updated`.
- [ ] The table supports search and scrolling.
- [ ] All data is read-only.
- [ ] `last_updated` reflects the actual date of latest admin-side refresh.

---

## Business Value

- Supports clinical accuracy by referencing standardized medical codes.
- Ensures all users have consistent and up-to-date terminology.
- Provides groundwork for service-to-diagnosis linking and future analytics.


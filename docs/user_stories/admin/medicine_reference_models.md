# Medicine Reference Models (Admin Panel)

---

## User Story: View Medical Dictionaries

### As an
Administrator with "medicine" access level

### I want to
View and synchronize standard medical reference data

### So that
I can ensure accurate, up-to-date information is available throughout the system

---

## Description

The following read-only reference dictionaries are grouped under the **Medicine** section in the admin panel:
- `ICD-10`
- `Relations`
- `Allergy Types`
- `Allergy Causes`
- `Allergy Reactions`

These models are **view-only** for all users. Only `superuser` has permission to **archive** or **unarchive** individual entries.

Each page provides:
- Table of entries (with archive status indicator)
- Detail view per entry (read-only)
- Sync, Export buttons
- Metadata about:
  - Last sync timestamp
  - User who performed the sync

### Available Actions:
- `Sync` (available to users with access):
  - ICD-10: from external service or uploaded file
  - Other dictionaries: from uploaded file
- `Export` formats:
  - `.csv`
  - `.xlsx`
  - `.json`

---

## ICD-10

### Table Columns:
- Code
- Name

### Detail View:
- Code
- Name

---

## Relations

### Table Columns:
- Name

### Detail View:
- Name

---

## Allergy Types / Causes / Reactions

### Table Columns:
- Name
- Code
- Source

### Detail View:
- Name
- Code
- Source

---

## Acceptance Criteria

- [ ] Users with `medicine` access can view each reference model
- [ ] All tables include appropriate columns per model
- [ ] Detail views are read-only
- [ ] Sync and Export buttons are available per model
- [ ] Sync fetches data from file or external service depending on model
- [ ] Export works in `.csv`, `.xlsx`, and `.json` formats
- [ ] Only superusers can archive or unarchive entries
- [ ] Last sync metadata is visible per page

---

## Business Value

- Centralizes and standardizes medical terminology across the platform
- Enables reliable syncing with verified external sources
- Supports compliance and data traceability


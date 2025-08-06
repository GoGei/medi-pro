# Geo Models (Admin Panel)

---

## User Story: Manage Geo Reference Models

### As an
Administrator with "geoModels" access level

### I want to
View, edit, import/export, and synchronize the `Country` and `Timezone` reference models

### So that
I can keep location-related data up to date across the system

---

## Description

Geo models include two separate reference entities:
- `Country`
- `Timezone`

Each model has its own dedicated page accessible from the **"Geo Models"** submenu in the admin navigation.

Only users with `geoModels` access level can interact with these reference lists.

Each page includes:
- A table view of all entries
- Action buttons:
  - `Import`
  - `Export`
  - `Sync`
- Info block showing:
  - Timestamp of last synchronization
  - User who performed it

---

## Country

### Table Columns:
- Name
- Code (ISO 2-letter)
- Code3 (ISO 3-letter)

### Detail/Edit Form Fields:
- Name
- Code
- Code3

### Synchronization:
- Performed from an internal **JSON source file**

---

## Timezone

### Table Columns:
- Label (e.g., `(GMT+02:00) Europe/Warsaw`)
- Offset (e.g., `+02:00`)
- Name (system zone name, e.g., `Europe/Warsaw`)

### Detail/Edit Form Fields:
- Label
- Offset
- Name

### Synchronization:
- Performed from the system’s standard `zoneinfo` library

---

## Acceptance Criteria

- [ ] Geo Models menu includes separate pages for `Country` and `Timezone`
- [ ] Users with `geoModels` access can view, edit, import, export, and sync data
- [ ] Each page includes last sync info (timestamp and user)
- [ ] Country form includes fields: name, code, code3
- [ ] Timezone form includes fields: label, offset, name
- [ ] Import and Export allow full backup and restore of list values
- [ ] Sync updates the list from predefined sources (JSON or `zoneinfo`)

---

## Business Value

- Maintains accurate and standardized geo-data across the platform
- Enables full admin-side control and traceability for changes
- Supports synchronization with trusted sources


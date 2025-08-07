# Access List (Admin Panel)

---

## User Story: Manage Role-Based Access Controls

### As a
Superuser or Administrator with "accessList" access level

### I want to
View and manage access permissions per application role

### So that
I can control what actions each role is allowed to perform across the system

---

## Description

The **Access List** section provides a matrix interface for managing access control settings. This section is only accessible to:
- Superusers (full control)
- Users with `accessList` permission level (view or edit depending on sub-permissions)

The matrix is structured by:
- **Applications** (grouped areas of the system)
- **Roles** (columns)
- **Actions** (rows, e.g., `view`, `edit`, `add`, `delete`, `sync`, etc.)

### Interface Behavior:
- Each cell in the matrix represents permission for a specific action under a role.
- If the current user has edit access:
  - Checkboxes are **clickable** to enable/disable the permission.
- If the current user only has view access:
  - Checkboxes are **disabled** (visually marked as "deactivated").

---

## Acceptance Criteria

- [ ] Only users with `accessList` access or superuser can view this section
- [ ] The page displays a list of applications
- [ ] Each application contains a permission matrix:
  - Roles as columns
  - Actions as rows
  - Checkboxes in cells to indicate access
- [ ] Superusers can edit any permission
- [ ] Users with only view rights see disabled checkboxes
- [ ] All changes made by editors are saved and reflected immediately

---

## Business Value

- Provides centralized and fine-grained control over application permissions
- Enables role-based access management without code changes
- Supports security and accountability by limiting permissions based on roles


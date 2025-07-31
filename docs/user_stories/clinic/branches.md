# Branch Management

---

## User Story: View Branch List

### As an
Employee

### I want to
See a list of branches I have access to

### So that
I can view clinic locations and related information

---

## Description

All employees, regardless of role, can view the list of branches.

Each branch entry shows:
- Name
- Region
- City
- Street
- Index

---

## Acceptance Criteria

- [ ] Any logged-in employee can view the branch list.
- [ ] Each branch displays its full address and name.
- [ ] Access is read-only unless the employee has `owner` role.

---

## User Story: Create Branch

### As an
Employee with the `owner` role

### I want to
Create a new branch

### So that
My clinic can expand to additional locations

---

## Description

An `owner` can create a branch by filling in the following fields:
- `name`
- `region` (selected from directory)
- `city` (selected from directory)
- `street` (free-text input)
- `index` (free-text input)

---

## Acceptance Criteria

- [ ] Only employees with the `owner` role can see the **"Create Branch"** button.
- [ ] The form includes required fields: name, region, city, street, index.
- [ ] After successful submission, the branch appears in the list.

---

## User Story: Edit Branch

### As an
Employee with the `owner` role

### I want to
Edit a branch’s details

### So that
I can update address or name when necessary

---

## Description

Owners can edit any existing branch by updating:
- `name`
- `region`
- `city`
- `street`
- `index`

---

## Acceptance Criteria

- [ ] Only employees with the `owner` role can see and access the **"Edit"** option.
- [ ] All editable fields are pre-filled with current data.
- [ ] Changes are saved only if validation passes.
- [ ] After saving, updated data appears in the branch list.

---

## User Story: Delete Branch

### As an
Employee with the `owner` role

### I want to
Delete a branch

### So that
I can remove branches that are no longer needed

---

## Description

Owners can delete a branch, but only after confirming the action.  
Some conditions may prevent deletion (see below).

**Blocking conditions:**
- The branch still has employees assigned to it.
- The branch has active appointments scheduled in the future.

---

## Acceptance Criteria

- [ ] Only employees with the `owner` role can initiate branch deletion.
- [ ] Deletion requires confirmation.
- [ ] If deletion is blocked by any condition, an error message explains why.
- [ ] The branch is removed from the list after successful deletion.

---

## Business Value

- Ensures controlled access to critical clinic structure.
- Protects data integrity by restricting destructive actions to authorized users.
- Enables scalable management of multiple clinic locations.

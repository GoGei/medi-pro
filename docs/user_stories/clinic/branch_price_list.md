# Price List Management

---

## User Story: View Price List

### As an
Employee

### I want to
View the list of services and categories offered by my branch

### So that
I can see what treatments or procedures are available and their prices

---

## Description

Each **branch** has its own **price list**, consisting of:

- `name` (title of the price list)
- One or more **categories**:
  - `name` of the category
  - One or more **services** inside each category:
    - `name`
    - `price`

When viewing:
- Categories are initially **collapsed**.
- Clicking a category expands to show its services and their prices.
- The entire price list is **read-only** for users without editing rights.

---

## Acceptance Criteria

- [ ] Any employee can view the price list of their branch.
- [ ] The price list is organized by categories and services.
- [ ] Categories are collapsed by default and expand on click.
- [ ] Each service displays its name and price.

---

## User Story: Edit Price List

### As an
Administrator or Owner

### I want to
Create and update categories and services within the price list

### So that
My branch offers up-to-date and structured service information

---

## Description

Authorized users can:
- Add, rename, or delete **categories**
- Add, edit, or remove **services** inside categories
- For each service, provide:
  - `name`
  - `price`
  - `ICD-10 service`

Changes are staged locally. Once editing is complete, the user clicks **Save**, and the full price list is saved at once.

---

## Acceptance Criteria

- [ ] Only `owner` or `administrator` roles can edit the price list.
- [ ] Services can be freely added or removed inside categories.
- [ ] Categories can be freely managed.
- [ ] Edits are saved only after clicking **Save**.
- [ ] A `code` field for services is optional and supports ICD-10/CDT or internal codes.

---

## User Story: Copy Price List to Another Branch

### As an
Administrator or Owner

### I want to
Duplicate an existing price list into another branch that doesn’t have one

### So that
I can reuse service structures without building from scratch

---

## Description

If a branch **does not have** a price list, the user can select another branch’s price list and **copy it**.

Restrictions:
- Copying is only allowed if the target branch has no price list.
- A confirmation prompt is shown before proceeding.

---

## Acceptance Criteria

- [ ] Only users with `owner` or `administrator` role can copy price lists.
- [ ] Copy is allowed only if the target branch has no price list.
- [ ] User selects a source branch and confirms the action.
- [ ] After copying, the target branch has an identical price list structure.

---

## Business Value

- Enables structured and easy-to-navigate service listings per branch.
- Simplifies setup of new branches by supporting price list reuse.
- Ensures only authorized users can make critical changes.
- Allows future expansion into medical coding systems without locking design.

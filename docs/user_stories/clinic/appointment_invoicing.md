# Appointment Invoicing

---

## User Story: Generate Invoice After Appointment Close

### As an
Employee (Doctor or Administrator)

### I want to
Automatically generate an invoice after completing an appointment

### So that
I can ensure services are billed correctly and payments are trackable

---

## Description

When an appointment is marked as **closed**, an **Invoice** is automatically created for the patient.

### Invoice content:
- List of all **performed services** with their **names** and **prices** (from the branch’s price list).
- For each service:
  - Associated **ICD-10 diagnosis** (if present).
  - Price next to each service.
- Total sum of all services.

### Invoice behavior:
- Any employee can **view** or **download PDF** version of the invoice at any time.
- The invoice can be **emailed** to the patient as a PDF attachment if an email is present in the system.
- Only employees with the role `administrator` can **mark the invoice as paid**.

### Payment options:
- When marking an invoice as paid, the following **payment types** are available:
  - `Card`
  - `Cash`

---

## Acceptance Criteria

- [ ] Invoice is generated automatically upon appointment close.
- [ ] Invoice includes all performed services, their ICD-10 codes (if any), and prices.
- [ ] Any employee can view and download the invoice PDF.
- [ ] Invoice can be sent to the patient’s email if it exists.
- [ ] Only administrators can set invoice status to `paid`.
- [ ] Payment type must be selected when marking as paid (Card or Cash).

---

## Business Value

- Ensures transparent billing based on actual performed services.
- Automates financial documentation and reporting.
- Reduces administrative effort while supporting compliance and record-keeping.


# Appointment Close Flow

---

## User Story: View and Manage Appointment Status

### As an
Employee

### I want to
View the details of any appointment and manage it if I'm the assigned doctor

### So that
I can provide services, record diagnoses, and properly close appointments

---

## Description

### Access Rules:
- Any employee can **view** an appointment.
- Only the **assigned doctor** (employee with role `doctor`) can **start** the appointment.
- Only the employee who **started** the appointment can **edit** and **close** it.

### Appointment Flow:
1. Appointment begins in status `new`.
2. The assigned doctor clicks **Start**, transitioning the status to `in_progress`.
3. During the appointment:
   - The doctor can select one or more **services** from the branch’s price list.
   - Each service can optionally have:
     - One ICD-10 **diagnose** attached.
     - Diagnosis must be labeled as **primary** or **secondary**.
   - An optional **comment** can be added.
4. When ready, the doctor clicks **Close**, which transitions the status to `done`.
   - At least **one service** must be selected to close the appointment.

---

## Acceptance Criteria

- [ ] Any employee can view any appointment.
- [ ] Only the assigned doctor can click **Start**.
- [ ] Only the employee who started the appointment can make changes or close it.
- [ ] Clicking **Start** changes the status to `in_progress`.
- [ ] Doctor can select services from the active branch price list.
- [ ] Services can be assigned zero or one ICD-10 service.
- [ ] ICD-10 codes service be labeled as `primary` or `secondary`.
- [ ] Comment field is optional.
- [ ] Clicking **Close** changes status to `done`, but only if at least one service is selected.

---

## Business Value

- Ensures role-based and secure handling of clinical sessions.
- Enforces minimum documentation of provided services.
- Supports diagnostic traceability through ICD-10 tagging.
- Prevents incomplete or improper appointment closure.


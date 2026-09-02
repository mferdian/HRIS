# InsightHR Odoo Field Mapping

This document maps the first InsightHR business data layer to existing Odoo 17 HR models. The goal is to reuse Odoo's native HR data model wherever possible and only add custom fields when there is a clear InsightHR business need.

## Classification

| Classification | Meaning |
| --- | --- |
| EXISTING | Available in Odoo and used directly by InsightHR. |
| ANALYTICS | Existing Odoo field that will be useful for future analytics, but is not extended in this phase. |
| CUSTOM | Not available as required, or needs InsightHR-specific business logic. |
| IGNORE | Internal or technical Odoo field outside the current InsightHR business scope. |

## Employee

| Domain | Model | Field | Classification | Purpose |
| --- | --- | --- | --- | --- |
| Employee | `hr.employee` | `name` | EXISTING | Employee name. |
| Employee | `hr.employee` | `work_email` | EXISTING | Work email address. |
| Employee | `hr.employee` | `work_phone` | EXISTING | Work phone number. |
| Employee | `hr.employee` | `mobile_phone` | EXISTING | Mobile contact number. |
| Employee | `hr.employee` | `department_id` | EXISTING | Employee department. |
| Employee | `hr.employee` | `job_id` | EXISTING | Current job position. |
| Employee | `hr.employee` | `parent_id` | EXISTING | Direct manager. |
| Employee | `hr.employee` | `coach_id` | EXISTING | Coach or mentor. |
| Employee | `hr.employee` | `company_id` | EXISTING | Employee company. |
| Employee | `hr.employee` | `resource_calendar_id` | ANALYTICS | Working schedule source for attendance analysis. |
| Employee | `hr.employee` | `tz` | ANALYTICS | Employee timezone context for future attendance calculations. |
| Employee | `hr.employee` | `active` | EXISTING | Archive status. |
| Employee | `hr.employee` | `employee_code` | CUSTOM | Stable business identifier separate from Odoo database ID. |
| Employee | `hr.employee` | chatter/activity fields | IGNORE | Odoo communication and activity metadata. |

## Contract

| Domain | Model | Field | Classification | Purpose |
| --- | --- | --- | --- | --- |
| Contract | `hr.contract` | `employee_id` | EXISTING | Links contract to employee. |
| Contract | `hr.contract` | `name` | EXISTING | Contract reference. |
| Contract | `hr.contract` | `date_start` | EXISTING | Contract start date. |
| Contract | `hr.contract` | `date_end` | EXISTING | Contract end date. |
| Contract | `hr.contract` | `state` | EXISTING | Contract lifecycle status. |
| Contract | `hr.contract` | `job_id` | EXISTING | Job position under the contract. |
| Contract | `hr.contract` | `department_id` | EXISTING | Department under the contract. |
| Contract | `hr.contract` | `resource_calendar_id` | ANALYTICS | Contract working schedule for attendance interpretation. |
| Contract | `hr.contract` | `wage` | ANALYTICS | Compensation context for future HR analytics where permitted. |
| Contract | `hr.contract` | accounting/internal fields | IGNORE | Not part of phase-one InsightHR mapping. |

## Attendance

| Domain | Model | Field | Classification | Purpose |
| --- | --- | --- | --- | --- |
| Attendance | `hr.attendance` | `employee_id` | EXISTING | Links attendance entry to employee. |
| Attendance | `hr.attendance` | `check_in` | EXISTING | Actual check-in datetime. |
| Attendance | `hr.attendance` | `check_out` | EXISTING | Actual check-out datetime. |
| Attendance | `hr.attendance` | `worked_hours` | ANALYTICS | Working-hours analysis input. |
| Attendance | `hr.attendance` | `overtime_hours` | EXISTING | Odoo-provided overtime value; do not duplicate. |
| Attendance | `hr.attendance` | `late_minutes` | CUSTOM | Future lateness duration derived from working schedules. |
| Attendance | `hr.attendance` | `early_leave_minutes` | CUSTOM | Future early-leave duration derived from working schedules. |
| Attendance | `hr.attendance` | `attendance_status` | CUSTOM | Future normalized attendance status once scheduling logic is validated. |
| Attendance | `hr.attendance` | technical/geolocation metadata | IGNORE | Not part of phase-one InsightHR extension. |

## Time Off

| Domain | Model | Field | Classification | Purpose |
| --- | --- | --- | --- | --- |
| Time Off | `hr.leave` | `employee_id` | EXISTING | Links leave request to employee. |
| Time Off | `hr.leave` | `holiday_status_id` | EXISTING | Leave type. |
| Time Off | `hr.leave` | `request_date_from` | EXISTING | Requested start date. |
| Time Off | `hr.leave` | `request_date_to` | EXISTING | Requested end date. |
| Time Off | `hr.leave` | `number_of_days` | ANALYTICS | Leave duration for future workforce analysis. |
| Time Off | `hr.leave` | `state` | EXISTING | Approval workflow status. |
| Time Off | `hr.leave` | allocation/internal workflow fields | IGNORE | Reuse Odoo workflow without custom duplication. |

## Recruitment

| Domain | Model | Field | Classification | Purpose |
| --- | --- | --- | --- | --- |
| Recruitment | `hr.job` | `name` | EXISTING | Job position name. |
| Recruitment | `hr.job` | `department_id` | EXISTING | Hiring department. |
| Recruitment | `hr.job` | `no_of_recruitment` | ANALYTICS | Hiring target for future recruitment analytics. |
| Recruitment | `hr.job` | `no_of_hired_employee` | ANALYTICS | Hiring result indicator. |
| Recruitment | `hr.applicant` | `partner_name` | EXISTING | Candidate name. |
| Recruitment | `hr.applicant` | `email_from` | EXISTING | Candidate email. |
| Recruitment | `hr.applicant` | `job_id` | EXISTING | Applied job. |
| Recruitment | `hr.applicant` | `stage_id` | ANALYTICS | Recruitment pipeline stage. |
| Recruitment | `hr.applicant` | `priority` | ANALYTICS | Candidate rating signal. |
| Recruitment | `hr.applicant` | `employee_id` | ANALYTICS | Link to employee after hiring when available. |

## Main Model Relationships

`hr.employee` is the central employee master record for InsightHR.

`hr.employee` -> `hr.contract` -> `resource.calendar`

The employee and contract working schedules are the source of truth for future attendance interpretation. InsightHR must not hard-code office hours.

`hr.employee` -> `hr.attendance`

Attendance records provide actual check-in and check-out datetimes. Future lateness and early-leave logic must compare these records against Odoo working intervals with timezone awareness.

`hr.employee` -> `hr.leave`

Time-off requests remain in the native Odoo leave workflow. InsightHR should reuse leave type, duration, and approval state.

`hr.job` -> `hr.applicant` -> `hr.employee`

Recruitment starts from job positions and applicants. Accepted applicants may become employees through Odoo's recruitment workflow.

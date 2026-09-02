# InsightHR Gap Analysis

This document compares phase-one InsightHR requirements with Odoo 17's native HR capabilities. The implementation principle is to extend existing Odoo models with `_inherit` when needed, and avoid rebuilding HRIS features that Odoo already provides.

| Feature | Odoo Model | Existing Support | Customization | Notes |
| --- | --- | --- | --- | --- |
| Employee Master | `hr.employee` | Yes | Minor | Extend existing employee model with a stable business identifier. |
| Employee Business Code | `hr.employee` | Partial | Yes | Odoo has database IDs and references, but InsightHR needs a manual stable code such as `EMP-00001`. |
| Department | `hr.department` via `hr.employee.department_id` | Yes | No | Reuse native relationship. Do not duplicate `department_name`. |
| Job Position | `hr.job` via `hr.employee.job_id` | Yes | No | Reuse native relationship. Do not duplicate `job_name`. |
| Manager | `hr.employee.parent_id` | Yes | No | Reuse native relationship. Do not duplicate `manager_name`. |
| Contract | `hr.contract` | Yes | No/Minor | Reuse existing model and lifecycle. |
| Working Schedule | `resource.calendar` via employee or contract | Yes | Future validation | Source of truth for attendance interpretation. |
| Attendance | `hr.attendance` | Yes | Minor/Future | Reuse check-in/check-out workflow. |
| Late Detection | `hr.attendance` + `resource.calendar` | Partial | Future | Requires validated working interval and timezone logic before implementation. |
| Early Leave Detection | `hr.attendance` + `resource.calendar` | Partial | Future | Requires validated schedule handling, including multiple intervals and shifts. |
| Overtime | `hr.attendance` | Yes | Avoid duplicate implementation | Odoo environment already provides `overtime_hours`; InsightHR must not recreate it. |
| Time Off | `hr.leave` | Yes | Minor/None | Reuse Odoo time-off workflow. |
| Recruitment | `hr.job`, `hr.applicant` | Yes | Minor | Reuse recruitment pipeline. |
| Promotion Scoring | - | No | Future | Analytics phase only; not implemented in phase one. |
| Employee Segmentation | - | No | Future | Analytics phase only; not implemented in phase one. |
| Training Recommendation | skills data + analytics | Partial | Future | Requires a later analytics/business rules phase. |
| Attendance Anomaly Detection | `hr.attendance` data | Partial | Future | Analytics phase only; not implemented in phase one. |
| HR Analytics Dashboard | multiple models | Partial | Future | Do not implement until business data layer is stable. |

## Minimum Phase-One Customization

Phase one adds only `employee_code` to `hr.employee`.

The field is intentionally manual in this phase. Auto-generation with sequences can be added later after the code format, migration rules, and business ownership are confirmed.

The field must be:

- `Char`
- indexed
- `copy=False`
- unique when provided
- not required, so existing employee records do not block module installation

## Attendance Design Deferred

The following attendance fields are recognized as InsightHR requirements but are not implemented in phase one:

- `late_minutes`
- `early_leave_minutes`
- `attendance_status`

The calculation design must be validated against Odoo 17 scheduling behavior before implementation:

- employee-level and contract-level `resource_calendar_id`
- calendar attendance intervals
- multiple work intervals in one day
- employee timezone and user timezone
- overnight shifts
- flexible schedules
- public holidays and approved leaves
- incomplete attendance records without `check_out`

Until those behaviors are validated in the running Odoo environment, InsightHR should not add hard-coded or misleading computed attendance values.

## Explicit Non-Goals For This Phase

The following are intentionally not implemented:

- analytics service
- machine learning models
- anomaly detection
- clustering or employee segmentation
- promotion scoring
- training recommendations
- custom analytics dashboard
- duplicate replacement models for Odoo HR, Attendance, Time Off, or Recruitment

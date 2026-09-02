# InsightHR

InsightHR is an HRIS foundation built on Odoo 17. The project currently focuses on establishing a clean Odoo business data layer before adding analytics or machine learning features.

## Architecture

- Odoo 17 runs as the main HR application.
- PostgreSQL 15 stores Odoo data.
- Custom Odoo modules are mounted from `./odoo/addons` into `/mnt/extra-addons`.
- Analytics service configuration exists as future groundwork, but the service is intentionally not enabled yet.

## Prerequisites

- Docker
- Docker Compose
- Git

## Environment Setup

Copy `.env.example` to `.env` when local secrets are needed.

Do not commit `.env`, database dumps, filestore archives, or generated credentials.

## Start Odoo

```bash
docker compose up -d
```

Odoo is exposed at:

```text
http://localhost:8069
```

PostgreSQL is exposed on host port `5433`.

## Install InsightHR Module

1. Start the Docker services.
2. Open Odoo at `http://localhost:8069`.
3. Create or select the target database.
4. Enable developer mode if needed.
5. Update the Apps List.
6. Search for `InsightHR`.
7. Install the module.

The module is located at:

```text
odoo/addons/insighthr
```

## Project Structure

```text
.
|-- docker-compose.yml
|-- docs
|   |-- gap-analysis.md
|   `-- odoo-field-mapping.md
`-- odoo
    `-- addons
        `-- insighthr
            |-- __init__.py
            |-- __manifest__.py
            |-- models
            `-- views
```

## Current Development Status

Completed:

- Docker foundation for Odoo 17 and PostgreSQL 15.
- Odoo field mapping documentation.
- InsightHR gap analysis documentation.
- Initial `insighthr` custom Odoo module.
- Manual `employee_code` field on `hr.employee`.

Not implemented yet:

- analytics service
- machine learning
- anomaly detection
- employee segmentation
- promotion scoring
- training recommendation
- analytics dashboard
- late or early-leave attendance calculations

Attendance calculations are deferred until Odoo 17 working schedules, resource calendars, timezones, shifts, and edge cases are validated in the runtime environment.

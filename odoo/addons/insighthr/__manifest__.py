{
    "name": "InsightHR",
    "summary": "InsightHR foundation extensions for Odoo HR",
    "description": """
InsightHR custom module foundation for Odoo 17.

This phase extends Odoo HR with a manual employee business code and prepares
clean extension points for future HR business logic.
""",
    "version": "17.0.1.0.0",
    "category": "Human Resources",
    "author": "Bhineka Inti Tekfonindo",
    "license": "LGPL-3",
    "depends": [
        "hr",
        "hr_attendance",
    ],
    "data": [
        "views/hr_employee_views.xml",
    ],
    "application": True,
    "installable": True,
}

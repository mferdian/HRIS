{
    "name": "InsightHR",
    "summary": "InsightHR foundation extensions for Odoo HR",
    "version": "17.0.1.0.0",
    "category": "Human Resources",
    "author": "Bhineka Inti Tekfonindo",
    "license": "LGPL-3",
    "depends": [
        "hr",
        "hr_attendance",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_employee_views.xml",
        "views/hr_attendance_views.xml",
    ],
    "application": True,
    "installable": True,
}

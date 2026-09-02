from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    employee_code = fields.Char(
        string="Employee Code",
        copy=False,
        index=True,
        help="Manual InsightHR business identifier, for example EMP-00001.",
    )

    _sql_constraints = [
        (
            "employee_code_unique",
            "unique(employee_code)",
            "Employee Code must be unique.",
        ),
    ]

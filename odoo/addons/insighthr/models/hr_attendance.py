from odoo import models


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    # Attendance lateness and early-leave metrics are intentionally deferred.
    # They must be derived from Odoo working schedules, intervals, and timezone
    # behavior after those rules are validated in the running Odoo 17 environment.

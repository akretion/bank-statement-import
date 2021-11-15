# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    date_create = fields.Date("Create Date")
    date_execution = fields.Date("Execution Date")
    date_internal = fields.Date("Internal Ref. Date")
    date_value = fields.Date("Value Date")
    date_update = fields.Date("Update Date")

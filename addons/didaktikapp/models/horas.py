from odoo import models, fields


class DidaktikAppHoras(models.Model):
    _name = 'didaktikapp.horas'
    _description = 'Horas trabajadas por empleado'


    employee_id = fields.Many2one(
        'hr.employee',
        string="Empleado",
        default=lambda self: self.env.user.employee_id,
        readonly=True
    )


    app_id = fields.Many2one(
        'didaktikapp.app',
        string="Aplicacion",
        required=True
    )


    fecha = fields.Date(
        string="Fecha",
        default=fields.Date.today,
        required=True
    )


    horas = fields.Float(
        string="Horas trabajadas",
        required=True
    )
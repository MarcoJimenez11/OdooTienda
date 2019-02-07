from odoo import models, fields, api, _


class Clientes(models.Model):
    _name = 'tienda.clientes'
    dni = fields.Char('Dni', required=True)
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    direccion = fields.Char('Dirección', required=False)
    poblacion = fields.Char('Población', required=False)
    provincia = fields.Char('Provincia', required=False)
    email = fields.Char('Email', required=True)

    def name_get(self):
        res = []
        for record in self:
            name = record.dni + ' - ' + record.nombre + ' ' + record.apellidos
            res.append((record.id, name))
        return res

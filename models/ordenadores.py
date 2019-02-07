from odoo import models, fields, api, _


class Ordenadores(models.Model):
    _name = 'tienda.ordenadores'
    cod = fields.Char('Codigo', required=True)
    descripcion = fields.Char('Modelo Ordenador', required=True)
    proveedor = fields.Many2one('tienda.proveedores', 'Proveedores')


    def name_get(self):
        res = []
        for record in self:
            name = record.cod + ' - ' + record.descripcion
            res.append((record.id, name))
        return res

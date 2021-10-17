# -*- coding: utf-8 -*-

from odoo import models, fields, api



class bibliotcaEstante(models.Model):
    _name = 'bibliotca.estante'

    name = fields.Char(string='Nombre del estante')
    libros_ids = fields.One2many('bibliotca.libros', 'estante_id', string='Libros')

class bibliotcaEstante(models.Model):
    _name = 'bibliotca.libros'

    estante_id = fields.Many2one('bibliotca.estante', string='Estante')
    
    name = fields.Char(string='Nombre del libro')
    type = fields.Selection([
        ('1', 'Horror'),
        ('2', 'Comedia'),
        ('3', 'Drama'),
        ('4', 'Fantasia'),
        ('5', 'Amor'),

    ], string='Categoria')
  
    disponible = fields.Boolean(string='Disponible')
# -*- coding: utf-8 -*-
from openerp import http

# class CustomModule0(http.Controller):
#     @http.route('/custom_module0/custom_module0/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_module0/custom_module0/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_module0.listing', {
#             'root': '/custom_module0/custom_module0',
#             'objects': http.request.env['custom_module0.custom_module0'].search([]),
#         })

#     @http.route('/custom_module0/custom_module0/objects/<model("custom_module0.custom_module0"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_module0.object', {
#             'object': obj
#         })
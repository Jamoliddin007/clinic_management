# -*- coding: utf-8 -*-
# from odoo import http


# class ClinicApp(http.Controller):
#     @http.route('/clinic_app/clinic_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clinic_app/clinic_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('clinic_app.listing', {
#             'root': '/clinic_app/clinic_app',
#             'objects': http.request.env['clinic_app.clinic_app'].search([]),
#         })

#     @http.route('/clinic_app/clinic_app/objects/<model("clinic_app.clinic_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clinic_app.object', {
#             'object': obj
#         })


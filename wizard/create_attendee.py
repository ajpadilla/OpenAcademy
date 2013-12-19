#-*- coding: utf-8 -*-

from osv import osv,fields
from tools.translate import _

class attendee_memory(osv.osv_memory):
   _name = 'openacademy.attendee.memory'
   _columns = {
                 'name': fields.char('Name',64),
                 'partner_id': fields.many2one('res.partner','Partner',required=True),
                 'wiz_id':fields.many2one('openacademy.create.attendee.wizard'),
}
attendee_memory()

class create_attendee_wizard(osv.osv_memory):
   _name = 'openacademy.create.attendee.wizard'

 
#create_attendee_wizard()

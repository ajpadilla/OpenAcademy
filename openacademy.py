#a-*- coding: utf-8 -*-

from osv import osv, fields

class course (osv.osv):
 _name = "openacademy.course"
 _columns = {
           "name" : fields.char("Course Title",128,required=True),
           "description" : fields.text("Description"),
          }
course()

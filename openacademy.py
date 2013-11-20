#-*- coding: utf-8 -*-

from osv import osv, fields

class course (osv.osv):
 _name = "openacademy.course"
 _columns = {
           "name" : fields.char("Course Title",128,required=True),
           "description" : fields.text("Description"),
         }
course()

class session(osv.osv):
  _name = "openacademy.session"
  _columns = {
       "name" : fields.char("Session Title", 128, required=True),
       "start_date": fields.date("Start Date"),
       "duration": fields.float("Duration", digits=(6,2), help="Duration in days"),
       "seats":fields.integer("eats number"),
      }
session()


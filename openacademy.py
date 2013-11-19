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
  _name = "openacademy.sesion"
  
  _columns = {
      'name' : fields.char('Session Title',128, required="True"),
      'start_date' : fields.date("Start Date")
      'duration' : fields.float('Duration',digit=(6,2),help="Duration in days"),
      'seats' : fields.integer("Seats number"),
    }
session()

class attendee(osv.osv):
  _name = "openacademy.attendee"
  
  _columns = {
  }
attendee()
  

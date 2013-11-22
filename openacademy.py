#-*- coding: utf-8 -*-

from osv import osv, fields

class course (osv.osv):
 _name = "openacademy.course"
 _description = "Course"
 _columns = {
           "name" : fields.char("Course Title",128,required=True),
           "responsible_id" : fields.many2one("res.users", string="Responsible",ondelete="set null"),
           "description" : fields.text("Description"),
           "session_ids" : fields.one2many("session", "course_id", "Session"),
         }
course()

class session(osv.osv):
  _name = "session"
  _description="Session"
  _columns = {
       "name" : fields.char("Session Title", 128, required=True),
       "start_date": fields.date("Start Date"),
       "duration" : fields.float("Duration", digits=(6,2), help="Duration in days"),
       "seats" : fields.integer("Seats number"),
       "instructor_id": fields.many2one("res.partner", "Instructor"),
       "course_id" : fields.many2one("openacademy.course", "Course",
        required=True, ondelete="cascade"),
      }
session()


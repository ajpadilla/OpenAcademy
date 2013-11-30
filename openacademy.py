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
  _name="session"
  _description="Session"

  def _get_remaining_seats_percent(self,seats,attendee_list):
      return seats and ((100.0 * (seats - len(attendee_list)))/ seats) or 0

  def _remaining_seats_percent(self,cr,uid,ids,field,arg,context=None):
      sessions = self.browse(cr,uid,ids,context=context)
      result = {}
      for session in sessions :
         result[session.id] = self._get_remaining_seats_percent(session.seats, session.attendee_ids)
      return result

  _columns = {
       "name" : fields.char("Session Title", 128, required=True),
       "start_date": fields.date("Start Date"),
       "duration" : fields.float("Duration", digits=(6,2), help="Duration in days"),
       "seats" : fields.integer("Seats number"),
       "attendee_ids": fields.one2many("attendee","session_id","Attendee"),
       "remaining_seats_percent":fields.function(_remaining_seats_percent,
						 method=True,type='float',
                                                 string="Remaining seats" 
                                                ),
       "instructor_id": fields.many2one("res.partner", "Instructor",
                                        domain=["|",("instructor","=",True),
                                                    ("category_id.name",
                                                     "in",
                                                     ("Teacher Level 1","Teacher Level 2"))
                                               ]
                                       ),
       "course_id" : fields.many2one("openacademy.course", "Course",
        required=True, ondelete="cascade"),
      }
session()

class attendee(osv.osv):
 _name = "attendee"
 _description="Attendee"
 _rec_name="partner_id"
 _columns = {
     "name" : fields.char("Name attendee",size=128),
     "partner_id" : fields.many2one("res.partner","Partner",required=True,ondelete="cascade"),
     "session_id" : fields.many2one("session","Session",required=True,ondelete="cascade"),
 }
attendee()

class Partner(osv.osv):
 _inherit = "res.partner"
 _columns = {
      "instructor" : fields.boolean("Instructor"),
       "session_ids": fields.many2many("session","attendee","partner_id","session_id","Sessions")
 }
Partner()


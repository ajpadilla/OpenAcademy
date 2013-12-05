#-*- coding: utf-8 -*-

from osv import osv, fields
import time
class course (osv.osv):
 _name = "openacademy.course"
 _description = "Course"

 def _check_description(self,cr,uid,ids,context=None): 
    courses=self.browse(cr,uid,ids,context=context)
    check = True
    for course in courses :
      if course.name == course.description:
         check=False
    return check

 _constraints = [(_check_description, 'Please use a different description',['name','description'])]

 _columns = {
           "name" : fields.char("Course Title",128,required=True),
           "responsible_id": fields.many2one("res.users", string="Responsible",ondelete="set null"),
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
   
  def onchange_remaining_seats(self,cr,uid,ids,seats,attendee_ids,context=None):
       result={}
       result={ 'value':{'remaining_seats_percent': self._get_remaining_seats_percent(seats,attendee_ids)}}
       if seats < 0 :
        result['warning']={'title':'Warning','message':'You cannot have negative seats',}

       return result 

  def _get_attendee_count(self, cr, uid, ids, name, args, context=None):
     res = {}
     for session in self.browse(cr, uid, ids, context=context):
	res[session.id] = len(session.attendee_ids)
     return res



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
       'attendee_count' : fields.function(_get_attendee_count,type="integer",string="attendee Count",method=True),
       'instructor_id': fields.many2one('res.partner', 'Instructor'),
       "course_id" : fields.many2one("openacademy.course", "Course",required=True, ondelete="cascade"),
      # 'active': fields.boolean('Active'),
      }
  _defaults = {'start_date': lambda *a : time.strftime('%Y-%m-%d'),}
  _sql_constraints = [('unique_name', 'unique(name)','Course Title must be unique')]
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


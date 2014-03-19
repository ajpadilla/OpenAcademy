
{
        "name": "Open Academy",
	"version": "1.0",
	"depends": ["base"],
	"author": "Author Name",
	"category": "Test",
	"description": """
	               	Open Academy module for managing trainings:
                        - training courses
                        - training sessions
                        - attendees registration
                        """, 
     	"update_xml": ["openacademy_view.xml",
                       "security/groups.xml",
                       "security/ir.model.access.csv",
                       "report/session_report.xml"],
	"installable": True,
	"active": True,
}


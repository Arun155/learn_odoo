from odoo import models, fields, api,_

class StudentModel(models.Model):
	_name="student.student"

	
	seq=fields.Char(string="sequnce",readonly=True, default=lambda self: 'New')
	name = fields.Char(string="Student Name:")
	addr=fields.Char(string="Address:")	
	phn=fields.Char(string="Contact No:")


	@api.model_create_multi
	def create(self, values):
		for value in values:
			if value.get('seq','New') == 'New':
				value['seq'] = self.env['ir.sequence'].next_by_code('student.student') or ('New')
		return super().create(values)		






			







	
	

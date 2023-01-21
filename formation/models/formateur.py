-- coding: utf-8 --
from datetime import date
from odoo import models, fields, api, _

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////// Trainer Class ///////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Trainer(models.Model):
_name = 'training.trainer'
_inherit = ['mail.thread', 'mail.activity.mixin']
_description = 'training.trainer'
_rec_name = 'name_trainer'

 id_trainer = fields.Char('Trainer ID', readonly=True, required=True, copy=False, index=True, default='New')
 name_trainer = fields.Char('Trainer Name')

 identity_card = fields.Integer('Identity Card')
 gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
 email = fields.Char('Email')
 phone = fields.Char('Phone')
 trainer_image = fields.Image("Image")
 #image_1920 = fields.Image("Image")
 id = fields.Integer()
 color = fields.Integer()

 active = fields.Boolean(string="Active", default=True)

 trainerdescription = fields.Html('Trainer Description', sanitize=True, strip_style=False, translate=True)
 training_session_id = fields.Many2one('training.training', "Session")


 Theme_id = fields.Many2one('training.theme', "Theme")


 @api.model
 def create(self, vals):
      vals['id_trainer'] = self.env['ir.sequence'].next_by_code('training.trainer') #or 'New'
      return super(trainer, self).create(vals)




 def action_send_mail(self):
      self.ensure_one()
      template_id = self.env.ref('training.email_template_trainer').id
      ctx = {
           'default_model': 'training.trainer',
           'default_res_id': self.id,
           'default_use_template': bool(template_id),
           'default_template_id': template_id,
           'default_composition_mode': 'comment',
           'email_to': self.email,
      }
      return {
           'type': 'ir.actions.act_window',
           'view_type': 'form',
           'view_mode': 'form',
           'res_model': 'mail.compose.message',
           'target': 'new',
           'context': ctx,
      }

 @api.model
 def default_get(self, fields):
      res = super(trainer, self).default_get(fields)

      res['training_session_id'] = self._context.get('active_id')

      return res

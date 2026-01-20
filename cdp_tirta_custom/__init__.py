from . import models

def post_init_hook(env):
    contact = env['res.partner'].sudo()
    contact.create({
            'name' : 'Lazada'
        })
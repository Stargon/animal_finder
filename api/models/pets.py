from flask_restplus import fields
from namespaces.pets import ns

pet_defintion = {
    'id': fields.Integer(
        required=True, description='Database ID', example=3, location='form'
    ),
    'name': fields.String(
        required=False, description="Pet Name", example='Root', location='form'
    ),
    'sex': fields.String(
        required=False, description='Sex', example='female', location='form'
    ),
    'color': fields.Integer(
        required=False, description='Color ID from color table', example=10, location='form'
    ),
    'status': fields.Integer(
        required=False, description='Status ID from status table', example=2, location='form'
    ),
    'originator': fields.Integer(
        required=False, description='Orignator ID from originator table', example=4, location='form'
    )
} 

get_entry = ns.model('get_entry', pet_defintion)
# get_nested = ns.model('get_nested', {'pets': fields.List(fields.Nested(get_entry))})
get_nested = ns.model('get_nested', {
    'pets': fields.List(fields.Nested(get_entry)),
})

get = ns.parser()
get.add_argument('id', type=int, required=False, help='Database ID', location='args')
get.add_argument('name', type=str, required=False, help='Name, if known', location='args')
get.add_argument('sex', type=str, required=False, help='Sex', location='args')
get.add_argument('color', type=int, required=False, help='Color', location='args')
get.add_argument('status', type=int, required=False, help='Found Status', location='args')
get.add_argument('originator', type=int, required=False, help='Originator', location='args')

# post = get.copy()
# post.remove_argument('id')
post = ns.parser()
post.add_argument('name', type=str, required=False, help='Name, if known', location='form')
post.add_argument('sex', type=str, required=False, help='Sex', location='form')
post.add_argument('color', type=int, required=False, help='Color', location='form')
post.add_argument('status', type=int, required=False, help='Found Status', location='form')
post.add_argument('originator', type=int, required=False, help='Originator', location='form')

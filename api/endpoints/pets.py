from flask_restplus import Resource, Api
from namespaces.pets import ns
import models.pets as api_models
from classes.pets import Pets

@ns.route("/")
class PetsClass(Resource):
    """Handles Pets model."""

    @ns.expect(api_models.get)
    @ns.marshal_with(api_models.pet, code=200)
    def get(self):
        """Return list of pets."""
        args = api_models.get.parse_args()
        p = Pets()
        return p.select(id=args.id, name=args.name, sex=args.sex, color=args.color, status=args.status, originator=args.originator)
    
    @ns.doc(body=api_models.post, parser=api_models.post)
    @ns.marshal_with(api_models.get_entry, code=201)
    def post(self):
        """Insert pet into pets database."""
        args = api_models.post.parse_args()
        p=Pets()
        new_id = p.insert(args)
        return p.select(id=new_id)

@ns.route('/<int:id>')
@ns.param('id', 'Database ID of pet')
class PetHandler(Resource):
    """Handles Pet model."""

    @ns.marshal_with(api_models.pet, code=200)
    def get(self, id):
        """Return pet."""
        p = Pets()
        return p.select(id=id)
    
    @ns.doc(body=api_models.pet)
    def patch(self, id):
        """Make change to pet field"""
        pass
    
    @ns.doc(description='Kill a pet')
    @ns.marshal_with(api_models.pet_delete, code=202)
    def delete(self, id):
        """Delete a pet from database."""
        p = Pets()
        try:
            message = p.delete(id=id)
            code=200
        except Exception as ex:
            message = "Could not delete id: {0} ({1})".format(id, ex)
            code=500
        return {'id': id, 'message': message}, code
from app_init import db
from app.models.user import User

class Contact(db.Document):
    """User db model.
        Fields:
        name -- name phone number holder
        email -- email of the user
        phone_no -- phone number
        user -- added by user
    """
    name = db.StringField(required=True)
    email = db.EmailField(unique=True,required=True)
    phone_no = db.StringField(required=True)
    user = db.ReferenceField(User)
    
    def to_json(self):
        """Method to jsonify the object."""
        return {
            "name": self.name,
            "email": self.email,
            "phone_no": self.phone_no 
        }
           
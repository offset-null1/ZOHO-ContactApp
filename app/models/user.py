import datetime
import secrets

from bson.json_util import default
from app_init import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Document):
    """User db model.
        Fields:
        email -- email of the user
        password -- encrypted password
        secret -- secret key
    """
    email = db.EmailField(unique=True,required=True)
    secret = db.StringField(unique=True,required=True)
    password = db.StringField(required=True)
  
    def to_json(self):
        """Method to jsonify the object."""
        return {
            "email": self.email  
        }
           
    def hash_password(self):
        """Method to hash the password entered by the user while registration."""
        self.password = generate_password_hash(self.password).decode('utf8')
 
    def check_password(self, password):
        """Method to check the password entered by user while logging in.
        
            Keyword arguments:
            password -- password entered
        """
        return check_password_hash(self.password, password)
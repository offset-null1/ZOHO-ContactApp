from flask import request, session
from flask_restful import Resource,reqparse
from app.models.user import User
from app.models.contact import Contact
import mongoengine
from bson.objectid import ObjectId

 
class ContactApi(Resource):
    '''
    Contact : route('/contact')
    Methods:
        get()->json
            op: query
        post()->json
            op: create
        delete()->json
            op: delete 
        put()->json
            op: update     
    ''' 
    def get(self):
        
        # if 'username' in session:
        user = session['secret']
        
        if user:
            try:
                u = User.objects.get(secret = user)
                c = Contact.objects.get(user=u.id)
                if not c:
                    return {'error': 'Data not found'}, 404
                res = [c_.to_json() for c_ in c]
                return res, 200
        
            except mongoengine.errors.DoesNotExist as e:
                return {'error': "User haven't added data"}, 404
        # else:
            # return {'error': 'You need to be logged in'}, 401
    
    def post(self): 
        
        data = request.get_json(force=True)
        email = data['email']
        name = data['name']
        phone_no = data['phone_no']
        user = session['secret']
        
        if user:

            try:
                u = User.objects.get(secret = user)
            except mongoengine.errors.DoesNotExist as e:
                return {'error': "User haven't added data"}, 404
            
            try:
                c = Contact(email=email,name=name, phone_no=phone_no, user=u.id)
                # added_by=ObjectId(session['userid'])
                c.user.save()
                c.save()

                return c.to_json(), 200

            except mongoengine.errors.NotUniqueError as e:
                return {'error': 'Database already exists'}, 409
      
        # else:
            # return {'error': 'You need to be logged in'}, 401
     
     
    def delete(self):
        data = request.get_json(force=True)
        email = data['email']
        name = data['name']
        user = session['secret']
        
        # if 'username' in session:
        if user:
            try:
                u = User.objects.get(secret = user)
            except mongoengine.errors.DoesNotExist as e:
                return {'error': "User haven't added data"}, 404
            
            if email and name:
                c = Contact.objects(email=email, name=name, user=u.id)
            elif email:
                c = Contact.objects(email=email, user=u.id)
            else:
                c = Contact.objects(name=name, user=u.id)

            if not c:
                return{'error': 'Data not found'}, 404
            else:
                c.delete()
            return {'status': 'Success'}, 200
            
        # else:
            # return {'error': 'You need to be logged in'}, 401
               
    def put(self):
        
        data = request.get_json(force=True)
        email = data['email']
        name = data['name']
        phone_no = data['phone_no']
        user = session['secret']
        
        # if 'username' in session:
        if user:
            try:    
                u = User.objects.get(secret = user)
            except mongoengine.errors.DoesNotExist as e:
                return {'error': "User haven't added data"}, 404
            
            if email :
                c = Contact.objects(email = email, user = u.id)
            if not c:
                return {'error': 'Data not found'},404
            
            c.update(email=email, name=name, phone_no=phone_no)
            # ,added_by=ObjectId(session['userid']))
            return c[0].to_json(), 200
        
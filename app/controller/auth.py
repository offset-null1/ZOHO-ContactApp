import datetime
import secrets
from flask import json, request, session
from app_init import app
from werkzeug import exceptions
from app.models.user import User
from flask_restful import Resource,reqparse
from flask import request
import mongoengine
from datetime import timedelta

class SignupApi(Resource):
  """Signup api for user registration.
     
     Methods:
        post()->json
            op: create 
"""
  def post(self):
    email = request.form.get('email')
    password = request.form.get('password')
    secret = request.form.get('secret')
    
    try:
      user = User(email=email, secret=secret, password=password)
    except mongoengine.errors.NotUniqueError as e:
      return {'error': 'User already exists'}, 409
    except mongoengine.DuplicateKeyError as e:
      return {'error': 'User already exists'}, 409

    if not user:
      raise Exception('Duplicate') 

    user.hash_password()
    user.save()
    id = user.id
    return {'id': str(id)}, 200

class LoginApi(Resource):
  """Login api for user login.
      session expires in 34hours
      session dict stores secret, userid 
    
     Methods:
        post()->json
            op: create
         
"""
  def post(self):
    email = request.form.get('email')
    password = request.form.get('password')

    try:
      user = User.objects.get(email=email)
      
    except mongoengine.errors.DoesNotExist as e:
      return json.jsonify({'error': 'User not found'}),404

    authorized = user.check_password(password)
    if not authorized:
       return json.jsonify({'error': 'Email or password invalid'}), 401

    session.permanent = True
    app.permanent_session_lifetime = timedelta(days=1,hours=10)
    session['secret'] = user.secret
    session['userid'] = str(user.id)
    return {'secret': user.secret,'session':session}, 200
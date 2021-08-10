#-Module imports--------------------------------------------------
from datetime import datetime
from enum import unique
from typing import Dict
from flask import Flask, request, session, redirect, jsonify, send_from_directory
from flask_cors import CORS 

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask_sessionstore import Session
from werkzeug.security import generate_password_hash, check_password_hash

import os
import socket
import yaml
#import json

import jwt


#-Custom Modules and mappers-------
#from reserved_instances import invoices, auth, api_helpers

#-Some Globals-----------------------------------------------------
curDir = os.path.dirname(os.path.realpath(__file__)) 
dbDir = os.path.join(os.curdir, "db")
dbFilePath = os.path.join(dbDir, "webauth.db")
if not os.path.isdir(dbDir): 
  os.makedirs(dbDir, exist_ok=True)

confFileDir = os.path.join(os.curdir, "config")
confFilePath = os.path.join(confFileDir, "app_config.yaml")
# if not os.path.isdir(confFileDir): 
#   os.makedirs(confFileDir, exist_ok=True)


#-Build the flask app object---------------------------------------WASN BRETT
app = Flask(__name__, static_url_path='', static_folder='dist' )
app.secret_key = "changeitxyz"
app.debug = True
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


#-SQL Alchemy for Sessions----------------------------------------
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' %dbFilePath
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY_TABLE'] = 'sessions'
app.config['SESSION_SQLALCHEMY'] = db

sessionStore = Session(app)
sessionStore.app.session_interface.db.create_all()


#-The SQL Alchemy--------------------------------------------------
class User(db.Model, SerializerMixin):
  
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(32), unique=True)
  email = db.Column(db.String(64), unique=True)
  company = db.Column(db.String(64))
  unit = db.Column(db.String(64))
  phone = db.Column(db.String(16), unique=True)
  address = db.Column(db.String(64))
  city = db.Column(db.String(64))
  zip = db.Column(db.Integer)
  password_hash = db.Column(db.String(128))


  role_id = db.Column(db.Integer, db.ForeignKey('roles.id') )
  role = db.relationship('Roles')
  
  requiredCols = ["username", "email", "company"]
  changeableCols = ["email", "company", "unit", "phone", "address", "city", "zip" ]
  dictCols = ["id", "username", "email", "company", "unit", "phone", "address", "city", "zip", "role_id", "role" ]

  def generate_password_hash(self, password):
    self.password_hash = generate_password_hash(password)

  def verify_password(self, password):
    return check_password_hash(self.password_hash, password)

  def __repr__(self):
    return '<User %r>' % self.username

#---------------------
class Roles(db.Model, SerializerMixin):

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(32), unique=True, nullable=False)
  description = db.Column(db.String(128))

  rolesDefi = [
    { "name": "user", "description": "App User" },
    { "name": "admin", "description": "App Admin" }
  ]

  def __repr__(self):
    return '<Roles %r>' % self.name

#---------------------
class Apps(db.Model, SerializerMixin):
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(32), unique=True)
  description = db.Column(db.String(256) )
  auth_url = db.Column(db.String(256) )
  app_url = db.Column(db.String(256) )
  jwt_secret = db.Column(db.String(64) )

  requiredCols = ["name", "auth_url", "app_url", "jwt_secret"]
  changeableCols = ["name", "description", "auth_url", "app_url", "jwt_secret"]
  dictCols = ["id", "name", "description", "auth_url", "app_url" ]

  def __repr__(self):
    return '<User %r>' % self.name


#-Helpers Section--------------------------------------------------
diableAuth = True

def create_base_roles():
  for role in Roles.rolesDefi:
    # print(role)
    
    roleChk = Roles.query.filter_by(name=role["name"]).first()
    if not roleChk:
      curRole = Roles(name=role["name"], description=role["description"])
      db.session.add(curRole)
      db.session.commit()
  


#-App Config and Access Management Section-----------------------
@app.before_first_request
def before_everything():
  # inf = "Do something here"
  db.create_all()
  create_base_roles()

#--------------------------------------
@app.before_request
def check_before_every_request():
  inf = "Do something here"

  if not diableAuth and request.path.startswith("/api/") and "username" not in session:
    reqObj = {
      "method": request.method,
      "path": request.path,
      "message": "Please authenticate / login",
      "status": 401
    }
    return jsonify(reqObj), 401 


#-The HTML serve part---------------------------------------------
@app.route('/', methods=["GET"])
def html_home_get():
  #return 'Hello from the App root'
  try:
    return app.send_static_file("index.html")
  except:
    return "<h2>Front-End not found in 'dist' folder<h2>"


#-The API Section-------------------------------------------------

@app.route('/api', methods=["GET"])
def api_home_get():
  reqObj = {
    "method": request.method,
    "path": request.path,
    "message": "Hello from the API",
    "status": 200
  }


  #-------------
  return jsonify(reqObj), 200 

#------------------------------------------------
@app.route('/api/users', methods=["GET"])
def api_users_get():
  reqObj = {
    "method": request.method,
    "path": request.path,
    "message": "",
    "status": 200
  }

  reqObj["data"] = []
  usersObj = User.query.all()
  for usr in usersObj:
    dic = usr.to_dict(rules=('-password_hash', '-role.description',))
    reqObj["data"].append(dic)

  #-------------
  return jsonify(reqObj), reqObj["status"]


#------------------------------------------------
@app.route('/api/users', methods=["POST"])
def api_users_post():
  reqObj = {
    "method": request.method,
    "path": request.path,
    "message": "",
    "status": 200
  }

  #-Validity Check---
  postIn = request.json
  if type(postIn) != dict:
    reqObj["status"] = 400
    reqObj["message"] = "Invalid Post Data"
    return jsonify(reqObj), reqObj["status"] 

  if "username" in postIn:
    usrObj = User.query.filter_by(username=postIn["username"]).first()
    if usrObj:
      reqObj["status"] = 409
      reqObj["message"] = "User '%s' already exists" %postIn["username"]
      return jsonify(reqObj), reqObj["status"] 

  neededKeys = []
  for key in User.requiredCols:
    if key not in postIn:
      neededKeys.append(key)
    elif len(postIn[key]) == 0:
      neededKeys.append(key)

  if len(neededKeys) > 0:
    reqObj["status"] = 400
    reqObj["message"] = "Following Values are required: %s" %neededKeys
    return jsonify(reqObj), reqObj["status"] 

  #------------------
  newUser = User(**postIn)
  db.session.add(newUser)
  db.session.commit()

  #------------------
  return jsonify(reqObj), reqObj["status"] 


#------------------------------------------------
@app.route('/api/users/<username>', methods=["GET"])
def api_user_get(username):
  reqObj = {
    "method": request.method,
    "path": request.path,
    "message": "",
    "status": 200
  }

  #-Validity Check---
  usrObj = User.query.filter_by(username=username).first()
  if not usrObj:
    reqObj["status"] = 404
    reqObj["message"] = "User '%s' not found" %username
    return jsonify(reqObj), reqObj["status"] 

  
  reqObj["data"] = usrObj.to_dict(rules=('-password_hash', '-role.description',))

  
  #-Netter Versuch ;) Wir nehmen aber lieber den SQLAlchemy Serializer! siehe oben
  # reqObj["data"] = {}
  # for key in User.dictCols:
  #   tmpRes = getattr(usrObj, key)
  #   #print(str(type(tmpRes)))
  #   if str(type(tmpRes)).startswith("<class '__main__"):
  #     tmpDict = {}
  #     print(dir(tmpRes))
  #     for atr in dir(tmpRes):
  #       try:
  #         tmpDict[atr] = getattr(tmpRes, atr)
  #       except:
  #         inf = "just a try"
  #     reqObj["data"][key] = tmpDict
  #   else:
  #     reqObj["data"][key] = getattr(usrObj, key)



  #------------------
  return jsonify(reqObj), reqObj["status"] 


#------------------------------------------------
@app.route('/api/users/<username>', methods=["PUT"])
def api_users_put(username):
  reqObj = {
    "method": request.method,
    "path": request.path,
    "message": "",
    "status": 200
  }

  #-Validity Check---
  postIn = request.json
  if type(postIn) != dict:
    reqObj["status"] = 400
    reqObj["message"] = "Invalid Post Data"
    return jsonify(reqObj), reqObj["status"] 
  
  #-Do it like Alchemy ;)
  usrObj = User.query.filter_by(username=username).first()
  if not usrObj:
    reqObj["status"] = 404
    reqObj["message"] = "User '%s' not found" %username
    return jsonify(reqObj), reqObj["status"] 

  for key, val in postIn.items():
    if key in User.changeableCols:
      setattr(usrObj, key, val)

  db.session.commit() 

  #------------------
  return jsonify(reqObj), reqObj["status"] 


#------------------------------------------------
@app.route('/api/users/<username>', methods=["DELETE"])
def api_users_delete(username):
  reqObj = {
    "method": request.method,
    "path": request.path,
    "message": "",
    "status": 200
  }

  #-Validity Check---
  usrObj = User.query.filter_by(username=username).first()
  if not usrObj:
    reqObj["status"] = 404
    reqObj["message"] = "User '%s' not found" %username
    return jsonify(reqObj), reqObj["status"] 

  db.session.delete(usrObj)
  db.session.commit() 

  #------------------
  return jsonify(reqObj), reqObj["status"] 


#------------------------------------------------
@app.route('/api/users/role', methods=["PUT"])
def api_users_role_put():
  reqObj = {
    "method": request.method,
    "path": request.path,
    "message": "",
    "status": 200
  }

  #-Validity Check---
  postIn = request.json
  try:
    username = postIn["username"]
    role = postIn["role"]
  except Exception as e:
    print(e)
    reqObj["status"] = 400
    reqObj["message"] = "Invalid Post Data"
    return jsonify(reqObj), reqObj["status"] 

  usrObj = User.query.filter_by(username=username).first()
  if not usrObj:
    reqObj["status"] = 404
    reqObj["message"] = "User '%s' not found" %username
    return jsonify(reqObj), reqObj["status"] 

  if type(role) == int:
    roleObj = Roles.query.filter_by(id=role).first()
  else:
    roleObj = Roles.query.filter_by(name=role).first()

  if not roleObj:
    reqObj["status"] = 404
    reqObj["message"] = "Role '%s' not found" %role
    return jsonify(reqObj), reqObj["status"] 

  #print(roleObj.description)

  #------------------
  usrObj.role = roleObj
  db.session.commit() 

  #------------------
  return jsonify(reqObj), reqObj["status"] 


#------------------------------------------------
@app.route('/api/users/auth', methods=["PUT"])
def api_users_auth_put():
  reqObj = {
    "method": request.method,
    "path": request.path,
    "message": "",
    "status": 200
  }

  #-Validity Check---
  postIn = request.json

  if "username" not in postIn or "password" not in postIn:
    reqObj["status"] = 400
    reqObj["message"] = "Invalid Post Data. Please provide username and password via JSON"
    return jsonify(reqObj), reqObj["status"] 

  curUsr = postIn["username"]
  curPwd = postIn["password"]
  
  usrObj = User.query.filter_by(username=curUsr).first()
  if not usrObj:
    reqObj["status"] = 404
    reqObj["message"] = "User '%s' not found" %curUsr
    return jsonify(reqObj), reqObj["status"] 
  
  #-Set the hash---
  usrObj.generate_password_hash(curPwd)
  db.session.commit()
 
  #------------------
  return jsonify(reqObj), reqObj["status"] 


#------------------------------------------------
@app.route('/api/users/auth', methods=["POST"])
def api_users_auth_post():
  reqObj = {
    "method": request.method,
    "path": request.path,
    "message": "",
    "status": 200
  }

  #-Validity Check---
  postIn = request.json

  if "username" not in postIn or "password" not in postIn:
    reqObj["status"] = 400
    reqObj["message"] = "Invalid Post Data. Please provide username and password via JSON"
    return jsonify(reqObj), reqObj["status"] 

  curUsr = postIn["username"]
  curPwd = postIn["password"]
  
  usrObj = User.query.filter_by(username=curUsr).first()
  if not usrObj:
    reqObj["status"] = 404
    reqObj["message"] = "User '%s' not found" %curUsr
    return jsonify(reqObj), reqObj["status"] 

  #-Password Verification---
  if not usrObj.password_hash:
    reqObj["status"] = 400
    reqObj["message"] = "User '%s' not activated" %curUsr
    return jsonify(reqObj), reqObj["status"] 
  
  pwdChk = usrObj.verify_password(curPwd)
  if not pwdChk:
    reqObj["status"] = 401
    reqObj["message"] = "Invalid credentials"
    return jsonify(reqObj), reqObj["status"]
  
  session["username"] = curUsr
  resDict = usrObj.to_dict(only=('role',))
  print(resDict)
  try:
    session["role"] = resDict["role"]["name"]
  except:
    reqObj["status"] = 401
    reqObj["message"] = "User '%s' has no valid role assigned" %curUsr
    return jsonify(reqObj), reqObj["status"] 

  reqObj["message"] = "User '%s' logged in via session. Role is: '%s'" % (session["username"], session["role"])

  #------------------
  return jsonify(reqObj), reqObj["status"] 


#------------------------------------------------
@app.route('/api/apps', methods=["GET"])
def api_apps_get():
  reqObj = {
    "method": request.method,
    "path": request.path,
    "message": "",
    "status": 200
  }

  reqObj["data"] = []
  appsObj = Apps.query.all()
  for app in appsObj:
    dic = app.to_dict(rules=('-jwt_secret',))
    reqObj["data"].append(dic)

  #-------------
  return jsonify(reqObj), reqObj["status"]


#------------------------------------------------
@app.route('/api/apps/<app>', methods=["GET"])
def api_app_get(app):
  reqObj = {
    "method": request.method,
    "path": request.path,
    "message": "",
    "status": 200
  }

  #-Validity Check---
  reqObj["data"] = []
  appObj = Apps.query.filter_by(name=app).first()
  if not appObj:
    reqObj["status"] = 404
    reqObj["message"] = "App '%s' not found" %app
    return jsonify(reqObj), reqObj["status"] 
 
  reqObj["data"] = appObj.to_dict(rules=('-jwt_secret', ))

  #-------------
  return jsonify(reqObj), reqObj["status"]


#------------------------------------------------
@app.route('/api/apps', methods=["POST"])
def api_apps_post():
  reqObj = {
    "method": request.method,
    "path": request.path,
    "message": "",
    "status": 200
  }

  #-Validity Check---
  postIn = request.json
  if type(postIn) != dict:
    reqObj["status"] = 400
    reqObj["message"] = "Invalid Post Data"
    return jsonify(reqObj), reqObj["status"] 

  if "name" in postIn:
    usrObj = Apps.query.filter_by(name=postIn["name"]).first()
    if usrObj:
      reqObj["status"] = 409
      reqObj["message"] = "App '%s' already exists" %postIn["name"]
      return jsonify(reqObj), reqObj["status"] 

  neededKeys = []
  for key in Apps.requiredCols:
    if key not in postIn:
      neededKeys.append(key)
    elif len(postIn[key]) == 0:
      neededKeys.append(key)

  if len(neededKeys) > 0:
    reqObj["status"] = 400
    reqObj["message"] = "Following Values are required: %s" %neededKeys
    return jsonify(reqObj), reqObj["status"] 

  #------------------
  newApp = Apps(**postIn)
  db.session.add(newApp)
  db.session.commit()

  #------------------
  return jsonify(reqObj), reqObj["status"] 


#------------------------------------------------
@app.route('/api/apps/<app>', methods=["PUT"])
def api_apps_put(app):
  reqObj = {
    "method": request.method,
    "path": request.path,
    "message": "",
    "status": 200
  }

  #-Validity Check---
  postIn = request.json
  if type(postIn) != dict:
    reqObj["status"] = 400
    reqObj["message"] = "Invalid Post Data"
    return jsonify(reqObj), reqObj["status"] 
  
  #-Do it like Alchemy ;)
  appObj = Apps.query.filter_by(name=app).first()
  if not appObj:
    reqObj["status"] = 404
    reqObj["message"] = "App '%s' not found" %app
    return jsonify(reqObj), reqObj["status"] 

  for key, val in postIn.items():
    if key in Apps.changeableCols:
      setattr(appObj, key, val)

  db.session.commit() 

  #------------------
  return jsonify(reqObj), reqObj["status"] 


#------------------------------------------------
@app.route('/api/apps/<app>', methods=["DELETE"])
def api_apps_delete(app):
  reqObj = {
    "method": request.method,
    "path": request.path,
    "message": "",
    "status": 200
  }

  #-Validity Check---
  usrObj = Apps.query.filter_by(name=app).first()
  if not usrObj:
    reqObj["status"] = 404
    reqObj["message"] = "App '%s' not found" %app
    return jsonify(reqObj), reqObj["status"] 

  db.session.delete(usrObj)
  db.session.commit() 

  #------------------
  return jsonify(reqObj), reqObj["status"] 


#------------------------------------------------

#------------------------------------------------



#-App Runner------------------------------------------------------
if __name__ == "__main__":
  
  app.run(host="0.0.0.0", port=5000)


  #context = ('./certs/app-scape.lab/crt/caweb.app-scape.lab.crt', './certs/app-scape.lab/key/caweb.app-scape.lab.key')
  # app.run(host="0.0.0.0", port=8443, ssl_context=context)
#------------------------------------------------------------------
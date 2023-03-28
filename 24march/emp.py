from flask import Flask,request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
api = Api(app) # we are using restful api


devices_args_parse = reqparse.RequestParser()
devices_args_parse.add_argument("name",type=str,help="device name has to given",required=True)
devices_args_parse.add_argument("status",type=bool,help="devicestatus")
 





class Device(Resource):#class which can be shared like a restful
    def get(self,empno):
        if empno==23:
            abort(404,message="invalid results")
        return {"message":"successfully added employee"}
    def post(self,empno):
        inputs=devices_args_parse.parse_args()
        return { "message" : "successfully updated employee"}
    def delete(self,empno):
        return { "message" : "deleted successfully"}
  

 #register this as a resource.
api.add_resource(Device,"/device/<int:empno>")   





app.run(debug=True) #dont use in production envrionment

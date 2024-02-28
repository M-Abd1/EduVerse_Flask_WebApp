from flask import request, Response, jsonify,session,render_template
from flask_restful import Resource
from databases.models import Courses,Teacher
from databases.models import Enroll
import requests

class EnrollAPI(Resource):
    def get(self):
        email = session.get("email")
        data = Enroll.objects.get(email=email)
        return Response(data.to_json(), mimetype="application/json", status=200)

class AdminApi(Resource):
    def get(self):
        try:
            courses=Courses.objects().to_json()
            return Response(courses, mimetype="application/json", status=200)
        except Exception as e:
            return Response(status=404)
    def post(self):
        name = request.form["name"]
        category = request.form["category"]
        duration = request.form["duration"]
        description = request.form["description"]

        course = Courses(name= name, category= category, duration= duration, description= description).save()
        id=course.id
        # #res={'id': str(id)}
        # return {"id": str(id)}, 200
        return Response(render_template("dashboard.html"))
        # return Response(inserted_course, mimetype="application/json", status=200)

class AdminApiTeacher(Resource):
    def get(self):
        try:
            teacher = Teacher.objects().to_json()
            return Response(teacher, mimetype="application/json", status=200)
        except Exception as e:
            return Response(status=404)
    def post(self):
        name = request.form["name"]
        email = request.form["email"]
        qualification = request.form[" qualification"]
        expertise = request.form[" expertise"]
        teacher= Teacher(name=name, email=email, qualification=qualification, expertise=expertise).save()
        id = teacher.id
        # #res={'id': str(id)}
        # return {"id": str(id)}, 200
        return Response(render_template("dashboard.html"))
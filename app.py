from flask import Flask , jsonify ,request,render_template,session,Response
from  databases import dbinitialization
from databases.models import Student,Contact,Enroll, Courses
from flask_restful import Resource, Api
from resources import routes


app = Flask(__name__)
app.config["SECRET_KEY"] = "13579"
# mongo engine settings
app.config["MONGODB_SETTINGS"] = {'host':"mongodb://localhost:27017/Education"}
# initialize mongo engine
dbinitialization.initialize_db(app)
api=Api(app)
routes.initialize_routes(api)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/teachers")
def teachers():
    return render_template("teachers.html")


@app.route("/contactform")
def contact_form():  # put application's code here
    return render_template("contact.html")

@app.route("/contact", methods = ["POST"])
def contact():
    try:
        if session.get("email"):
            name = request.form["name"]
            number = request.form["number"]
            message = request.form["message"]
            c1 = Contact(name=name, number=number, email=session.get("email"), message=message)
            c1.save()
            return render_template("contact.html",message="Message sent successfully!!!")
        else:
            return render_template("login.html")
    except Exception as e:
        res = {'id': str(c1.id), "inserted": "Failed to sent message!!!"}
        return jsonify(res)

@app.route("/course-1")
def course_1():
    return render_template("course-1.html")


@app.route("/course-2")
def course_2():
    return render_template("course-2.html")


@app.route("/course-3")
def course_3():
    return render_template("course-3.html")


@app.route('/loginform')
def loginform():
    return render_template("login.html")

@app.route('/login',methods=["POST"])
def login():
    try:
       email = request.form["email"]
       password=request.form["password"]
       d_data=Student.objects(email=email,password=password)
       if d_data:
           session["email"] = email
           if email == "admin@gmail.com":
                return render_template("dashboard.html")
           else:# name = session.get("name")
                return render_template("home.html", name = "Welcome to our website")
       else:
           return render_template("signup.html" , error = "Please Sign Up First or Wrong Password!")
    except Exception as e:
        res = {'id': str(d_data.id), "inserted": "Failed"}
        return jsonify(res)
    # try:
    #    email = request.form["email"]
    #    password=request.form["password"]
    #    d_data=Student.objects(email=email,password=password)
    #    if d_data:
    #        session["email"] = email
    #        # name = session.get("name")
    #        return render_template("home.html", name = "Welcome To Our Website")
    #    else:
    #        return render_template("signup.html" , error = "Please Sign Up First!")
    # except Exception as e:
    #     res = {'id': str(d_data.id), "inserted": "Failed"}
    #     return jsonify(res)

# @app.route('/login',methods=["POST"])
# def login():
#     email = request.form["Email"]
#     pwd = request.form["Password"]
#     student = Student.objects(email = email,password = pwd)
#     if student:
#         return render_template("home.html")
#     else:
#         return render_template("signup.html",error="Please Sign Up First!!")
@app.route('/signupform')
def signupform():
    return render_template("signup.html")


@app.route("/signup",methods=["POST"])
def signup():
    try:
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        contactNo = request.form["contactNo"]
        email = request.form["email"]
        password = request.form["password"]
        d_data = Student.objects(email=email).first()
        if d_data:
            return render_template("signup.html",error="Email already exists")
            # redirect("/signupform")
        else:
            session["email"] = email
            session["name"] = str(firstName)+ " " +str(lastName)
            name = session.get("name")
            student = Student(firstName=firstName, lastName=lastName, contactNo=contactNo, email=email,
                              password=password)
            student.save()
            return render_template("home.html",name="Welcome, " + name)

        # res = {'id': str(student.id), "inserted": "Done"}
        # return jsonify(res)

    except Exception as e:
        res = {'id': str(student.id), "inserted": "Failed"}
        return jsonify(res)
@app.route("/showdata")
def showdata():
    try:
        email = session.get("email")
        enroll = Enroll.objects(email=email)
        return Response(enroll.to_json(), mimetype="application/json", status=200)
    except Exception as e:
        return Response(404)

@app.route("/showcourses")
def showcourses():
    try:
        email = session.get("email")
        if email:
            courses = Courses.objects()
            return Response(courses.to_json(), mimetype="application/json", status=200)
    except Exception as e:
        return Response(404)

@app.route("/enroll", methods=["POST"])
def enroll():
    try:
        if session.get("email"):
            bank = request.form["bank"]
            transactionNo = request.form["transactionNo"]
            d_data = Enroll.objects(transactionNo=transactionNo).first()
            if d_data:
                return render_template("enroll.html", message= "Wrong Transcation Id!!!")
            contactNo = request.form["contactNo"]
            cnicNo = request.form["cnicNo"]
            category = request.form["category"]
            course = request.form["course"]

            e1 = Enroll(bank=bank, transactionNo=transactionNo, contactNo=contactNo,cnicNo=cnicNo,category=category,course=course,email=session.get("email"))
            e1.save()
            return render_template("enroll.html")
        else:
            return render_template("login.html")
    except Exception as e:
        res = {'id': str(e1.id), "inserted": "Failed"}
        return jsonify(res)

@app.route("/enrollform")
def enrollform():
    if session.get("email"):
        return render_template("enroll.html")
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return render_template("login.html")

@app.route("/addcoursesform")
def addcoursesform():
    return render_template("addcourses.html")

@app.route("/addteacherform")
def addteacherform():
    return render_template("addteacher.html")

# @app.route("/api/adminapi")
# def addcourse():
#
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == '__main__':
    app.run()

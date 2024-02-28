from .dbinitialization import db
class Student(db.Document):
    firstName= db.StringField(required=True)
    lastName = db.StringField(required=True)
    email = db.StringField(required=True)
    contactNo = db.StringField(required=True)
    password = db.StringField(required=True)

class Contact(db.Document):
    name=db.StringField(required=True)
    number=db.IntField(required=True)
    email=db.StringField(required=True)
    message=db.StringField(required=True)

class Enroll(db.Document):
    bank = db.StringField(required=True)
    transactionNo= db.StringField(required=True)
    contactNo=db.StringField(required=True)
    cnicNo=db.StringField(required=True)
    category=db.StringField(required=True)
    course = db.StringField(required =True)
    email= db.StringField(required=True)

class Courses(db.Document):
    name=db.StringField(required=True)
    category=db.StringField(required=True)
    duration=db.StringField(required=True)
    description=db.StringField(required=True)

class Teacher(db.Document):
    name=db.StringField(required=True)
    email = db.StringField(required=True)
    qualification=db.StringField(required=True)
    expertise=db.StringField(required=True)

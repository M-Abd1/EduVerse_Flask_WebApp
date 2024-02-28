from .resources import  EnrollAPI,AdminApi,AdminApiTeacher

def initialize_routes(api):
    api.add_resource(EnrollAPI, '/api/enroll')
    api.add_resource(AdminApi, '/api/adminapi')
    api.add_resource(AdminApiTeacher, '/api/adminapiteacher')
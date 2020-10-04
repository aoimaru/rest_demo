from flask_restful import Resource, reqparse, abort

from flask import jsonify

from src.models.deta_models import Student, StudentSchema


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class StudentListAPI(Resource):
    def get(self):
        query = session.query(Student).all()
        result = StudentSchema(many=True).dump(query)
        return result
    def post(self):
        args = request.json
        student_name = args["name"]
        session.add(Student(name=student_name))
        session.commit()
        return student_name

class StudentIdAPI(Resource):
    def get(self,index):
        result = session.query(Student).get(index)
        if result is None:
            abort(404)

        res = StudentSchema().dump(result)
        return res

    def put(self,index):
        result = session.query(Student).get(index)
        if result is None:
            abort(404)
        args = request.json
        new_student_name = args["name"]
        result.name = new_student_name
        session.commit()
        new_result = session.query(Student).get(index)
        res = StudentSchema().dump(new_result)
        return res

    def delete(self,index):
        result = session.query(Student).get(index)
        if result is None:
            abort(404)
        session.delete(result)
        session.commit()
        return None, 204




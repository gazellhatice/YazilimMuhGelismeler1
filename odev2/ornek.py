from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def __init__(self):
        self.data = pd.read_csv('kullanicilar.csv')
    def get(self):
        self.data = self.data.to_dict('records')
        return {'data' : self.data}, 200

    def post(self):
        data_arg=reqparse.RequestParser()
        data_arg.add_argument("name" , type=str)
        data_arg.add_argument("age" , type=int)
        data_arg.add_argument("city" , type=str)

        args = data_arg.parse_args()

        self.data = pd.concat([self.data, pd.DataFrame([args])], ignore_index=True)
        self.data.to_csv("kullanicilar.csv", index=False)
        
        return {'message' : 'Record successfully added.'}, 200

    def delete(self):
        name = request.args['name']

        if name in self.data['name'].values:
            self.data = self.data[self.data['name'] != name]
            self.data.to_csv('kullanicilar.csv', index=False)
            return {'message': 'Record successfully deleted.'}, 200
        else:
            return {'message': 'Record not found.'}, 404

class Cities(Resource):
    def get(self):
        data = pd.read_csv('kullanicilar.csv',usecols=[2])
        data = data.to_dict('records')
        return {'data' : data}, 200

class Name(Resource):
    def get(self,name):
        data = pd.read_csv('kullanicilar.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['name'] == name :
                return {'data' : entry}, 207
        return {'message' : 'No entry found with this name !'}, 405

# CSV dosyasından yaşların toplamını alan endpoint
class Sum(Resource):
    def get(self):
        data = pd.read_csv('kullanicilar.csv')
        total_age = data['age'].sum()
        return {'total_age': total_age}, 200

# CSV dosyasından yaşların çarpımını alan endpoint
class Multiply(Resource):
    def get(self):
        data = pd.read_csv('kullanicilar.csv')
        product_age = data['age'].prod()
        return {'product_age': product_age}, 200


# Add URL endpoints
api.add_resource(Users, '/users')
api.add_resource(Cities, '/cities')
api.add_resource(Name, '/<string:name>')
api.add_resource(Sum, '/sum')          # Yaşların toplamını döndüren endpoint
api.add_resource(Multiply, '/multiply')  # Yaşların çarpımını döndüren endpoint


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=5000) 
     app.run(port=46)  # 46 numaralı portta çalışacak

from flask import Flask
from flask_restful import Api
import models
import models.user as model_user
import routs.param as routs_param
import routs.user as routs_user

app = Flask(__name__)
api = Api(app)

api.add_resource(routs_param.ParamUrl, '/api/parameters/<user_name>/<type_name>/<type>')
api.add_resource(routs_user.GetUserParams, '/api/parameters/<user_name>')

if __name__ == '__main__':
    models.init_db()
    model_user.create_test_users(n=10)
    app.run(debug=False)

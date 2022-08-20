from main import app
from flask import render_template, request

import models.user as model_user
import models.param as model_param
import schemas.user as schema_user
import schemas.param as schema_param
from marshmallow import ValidationError


@app.route('/', methods=['POST', 'GET'])
def test_api():
    if request.method == 'POST':
        schema = schema_user.AddUserSchema()
        try:
            user_name = request.form['user_name']
            schema.load({'user_name': user_name})
            model_user.add_user(user_name)
        except ValidationError as exc:
            print(exc)
    users = model_user.get_all_user()
    return render_template('index.html', users=users), 200


@app.route('/add_param', methods=['POST'])
def add_param():
    schema_p = schema_param.ParamSchema()
    schema_u = schema_user.UserSchema()
    try:
        data = {'name': request.form['name'],
                'type': request.form['type'],
                'value': request.form['value']
                }
        user_name = request.form['user_name']
        param_update = schema_p.load(data)
        schema_u.load({'name': user_name})
        model_param.update_param(user_name, param_update=param_update)
    except BaseException as er:
        print(er)

    users = model_user.get_all_user()
    return render_template('index.html', users=users), 200

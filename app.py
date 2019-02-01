from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI'] = 'postgresql://abadojack@localhost:5432/playground_db'

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reward_name = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users', backref='rewards')


class UserSchema(ma.ModelSchema):
    class Meta:
        model = Users


class RewardSchema(ma.ModelSchema):
    class Meta:
        model = Reward


@app.route('/')
def index():
    one_user = Users.query.first()
    output = UserSchema().dump(one_user).data
    return jsonify({'user': output})


if __name__ == '__main__':
    app.run(debug=True)

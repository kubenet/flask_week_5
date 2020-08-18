from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CSRF_ENABLED = True
SECRET_KEY = 'b706835de79a2b4e80506f582af3676a'
app.secret_key = 'b706835de79a2b4e80506f582af3676a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
WTF_CSRF_SECRET_KEY = 'b706835de79a2b4e80506f582af3676a'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
